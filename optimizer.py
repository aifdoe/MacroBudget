import sys
from pathlib import Path

from data_loader import load_foods, load_settings
from optimization_model import build_and_solve_model
from result_builder import build_result
from result_exporter import export_result_to_json
from result_printer import print_results

FOODS_FILE = Path("foods.csv")
SETTINGS_FILE = Path("settings.json")
RESULT_FILE = Path("result.json")

KG_TO_LB = 2.20462


def calculate_targets(settings):
    bodyweight_kg = settings["bodyweight_kg"]
    bodyweight_lb = bodyweight_kg * KG_TO_LB

    calories_min = settings["calories_min"]
    calories_max = settings["calories_max"]

    protein_min = settings["protein_min_per_lb"] * bodyweight_lb
    protein_max = settings["protein_max_per_lb"] * bodyweight_lb

    fat_min = settings["fat_min_per_lb"] * bodyweight_lb
    fat_max = settings["fat_max_per_lb"] * bodyweight_lb

    return {
        "calories_min": calories_min,
        "calories_max": calories_max,
        "protein_min": protein_min,
        "protein_max": protein_max,
        "fat_min": fat_min,
        "fat_max": fat_max,
    }


def main():
    settings = load_settings(SETTINGS_FILE)
    foods = load_foods(FOODS_FILE)

    targets = calculate_targets(settings)

    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(
        foods,
        targets["calories_min"],
        targets["calories_max"],
        targets["protein_min"],
        targets["protein_max"],
        targets["fat_min"],
        targets["fat_max"],
    )

    result = build_result(
        model,
        foods,
        food_vars,
        total_cost,
        total_calories,
        total_protein,
        total_fat,
    )

    export_result_to_json(result, RESULT_FILE)
    print_results(result, targets)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)