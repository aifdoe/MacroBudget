import csv
from pathlib import Path

import pulp


FOODS_FILE = Path("foods.csv")

# User target settings
BODYWEIGHT_KG = 64.33
CALORIES_MIN = 2700
CALORIES_MAX = 2750

PROTEIN_MIN_PER_LB = 0.8
PROTEIN_MAX_PER_LB = 1.0

FAT_MIN_PER_LB = 0.3
FAT_MAX_PER_LB = 0.5

KG_TO_LB = 2.20462
BODYWEIGHT_LB = BODYWEIGHT_KG * KG_TO_LB

PROTEIN_MIN = PROTEIN_MIN_PER_LB * BODYWEIGHT_LB
PROTEIN_MAX = PROTEIN_MAX_PER_LB * BODYWEIGHT_LB

FAT_MIN = FAT_MIN_PER_LB * BODYWEIGHT_LB
FAT_MAX = FAT_MAX_PER_LB * BODYWEIGHT_LB


def load_foods(file_path):
    foods = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            food = {
            "name": row["name"],
            "price_per_kg": float(row["price_per_kg"]),
            "kcal_per_100g": float(row["kcal_per_100g"]),
            "protein_per_100g": float(row["protein_per_100g"]),
            "fat_per_100g": float(row["fat_per_100g"]),
            "max_grams_per_day": float(row["max_grams_per_day"]),
        }

            foods.append(food)

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


def print_results(model, food_vars, total_cost, total_calories, total_protein, total_fat):
    print("Status:", pulp.LpStatus[model.status])
    print()

    print("Targets:")
    print(f"Calories: {CALORIES_MIN:.0f}-{CALORIES_MAX:.0f} kcal")
    print(f"Protein: {PROTEIN_MIN:.1f}-{PROTEIN_MAX:.1f} g")
    print(f"Fat: {FAT_MIN:.1f}-{FAT_MAX:.1f} g")
    print()

    if pulp.LpStatus[model.status] != "Optimal":
        print("No optimal solution found.")
        return

    print("Food amounts per day:")

    for food_name, variable in food_vars.items():
        grams = variable.value()

        if grams > 0.01:
            print(f"{food_name}: {grams:.1f} g")

    print()
    print(f"Total cost: {pulp.value(total_cost):.2f} SEK/day")
    print(f"Total calories: {pulp.value(total_calories):.0f} kcal")
    print(f"Total protein: {pulp.value(total_protein):.1f} g")
    print(f"Total fat: {pulp.value(total_fat):.1f} g")


def main():
    foods = load_foods(FOODS_FILE)
    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(foods)
    print_results(model, food_vars, total_cost, total_calories, total_protein, total_fat)


if __name__ == "__main__":
    main()
    