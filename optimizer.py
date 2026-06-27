import csv
import json
import sys
from pathlib import Path

import pulp

from validation import (
    parse_food_name,
    parse_non_negative_number,
    parse_positive_number,
    validate_food_columns,
    validate_foods,
    validate_settings,
)

FOODS_FILE = Path("foods.csv")
SETTINGS_FILE = Path("settings.json")


def load_settings(file_path):
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            settings = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"Settings file not found: {file_path}")
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in {file_path}: line {error.lineno}")

    validate_settings(settings)

    return settings


try:
    settings = load_settings(SETTINGS_FILE)
except ValueError as error:
    print(f"Error: {error}")
    sys.exit(1)

BODYWEIGHT_KG = settings["bodyweight_kg"]
CALORIES_MIN = settings["calories_min"]
CALORIES_MAX = settings["calories_max"]

PROTEIN_MIN_PER_LB = settings["protein_min_per_lb"]
PROTEIN_MAX_PER_LB = settings["protein_max_per_lb"]

FAT_MIN_PER_LB = settings["fat_min_per_lb"]
FAT_MAX_PER_LB = settings["fat_max_per_lb"]

KG_TO_LB = 2.20462
BODYWEIGHT_LB = BODYWEIGHT_KG * KG_TO_LB

PROTEIN_MIN = PROTEIN_MIN_PER_LB * BODYWEIGHT_LB
PROTEIN_MAX = PROTEIN_MAX_PER_LB * BODYWEIGHT_LB

FAT_MIN = FAT_MIN_PER_LB * BODYWEIGHT_LB
FAT_MAX = FAT_MAX_PER_LB * BODYWEIGHT_LB


def load_foods(file_path):
    foods = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            validate_food_columns(reader.fieldnames)

            for row_number, row in enumerate(reader, start=2):
                food = {
                    "name": parse_food_name(row["name"], row_number),
                    "price_per_kg": parse_non_negative_number(row["price_per_kg"], "price_per_kg", row_number),
                    "kcal_per_100g": parse_non_negative_number(row["kcal_per_100g"], "kcal_per_100g", row_number),
                    "protein_per_100g": parse_non_negative_number(row["protein_per_100g"], "protein_per_100g", row_number),
                    "fat_per_100g": parse_non_negative_number(row["fat_per_100g"], "fat_per_100g", row_number),
                    "max_grams_per_day": parse_positive_number(row["max_grams_per_day"], "max_grams_per_day", row_number),
                }

                foods.append(food)

    except FileNotFoundError:
        raise ValueError(f"Foods file not found: {file_path}")

    validate_foods(foods)

    return foods


def build_and_solve_model(foods):
    model = pulp.LpProblem("MacroBudget", pulp.LpMinimize)

    food_vars = {}

    for food in foods:
        food_name = food["name"]

        food_vars[food_name] = pulp.LpVariable(
            name=f"grams_{food_name}",
            lowBound=0,
            upBound=food["max_grams_per_day"],
            cat="Continuous",
        )

    total_cost = pulp.lpSum(
        food_vars[food["name"]] * food["price_per_kg"] / 1000
        for food in foods
    )

    total_calories = pulp.lpSum(
        food_vars[food["name"]] * food["kcal_per_100g"] / 100
        for food in foods
    )

    total_protein = pulp.lpSum(
        food_vars[food["name"]] * food["protein_per_100g"] / 100
        for food in foods
    )

    total_fat = pulp.lpSum(
        food_vars[food["name"]] * food["fat_per_100g"] / 100
        for food in foods
    )

    model += total_cost

    model += total_calories >= CALORIES_MIN
    model += total_calories <= CALORIES_MAX

    model += total_protein >= PROTEIN_MIN
    model += total_protein <= PROTEIN_MAX

    model += total_fat >= FAT_MIN
    model += total_fat <= FAT_MAX

    model.solve(pulp.PULP_CBC_CMD(msg=False))

    return model, food_vars, total_cost, total_calories, total_protein, total_fat


def print_results(model, foods, food_vars, total_cost, total_calories, total_protein, total_fat):
    status = pulp.LpStatus[model.status]

    print("Status:", status)
    print()

    print("Targets:")
    print(f"Calories: {CALORIES_MIN:.0f}-{CALORIES_MAX:.0f} kcal")
    print(f"Protein: {PROTEIN_MIN:.1f}-{PROTEIN_MAX:.1f} g")
    print(f"Fat: {FAT_MIN:.1f}-{FAT_MAX:.1f} g")
    print()

    if status == "Infeasible":
        print("No feasible solution found.")
        print("The current food list and constraints cannot satisfy the selected targets.")
        print("Try widening the calorie or macronutrient ranges, increasing food max limits, or adding more foods.")
        return

    if status == "Unbounded":
        print("The model is unbounded.")
        print("This usually means the optimization problem is missing an important constraint.")
        return

    if status != "Optimal":
        print("No optimal solution found.")
        print("Solver status:", status)
        return

    print("Food amounts per day:")

    for food in foods:
        food_name = food["name"]
        variable = food_vars[food_name]
        grams = variable.value()

        if grams > 0.01:
            cost = grams * food["price_per_kg"] / 1000
            print(f"{food_name}: {grams:.1f} g ({cost:.2f} SEK)")

    print()
    print(f"Total cost: {pulp.value(total_cost):.2f} SEK/day")
    print(f"Total calories: {pulp.value(total_calories):.0f} kcal")
    print(f"Total protein: {pulp.value(total_protein):.1f} g")
    print(f"Total fat: {pulp.value(total_fat):.1f} g")


def main():
    foods = load_foods(FOODS_FILE)
    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(foods)
    print_results(model, foods, food_vars, total_cost, total_calories, total_protein, total_fat)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Error: {error}")
    