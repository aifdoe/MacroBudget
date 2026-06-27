import sys
from pathlib import Path

from data_loader import load_foods, load_settings
from optimization_model import build_and_solve_model
from result_printer import print_results

FOODS_FILE = Path("foods.csv")
SETTINGS_FILE = Path("settings.json")


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


def main():
    foods = load_foods(FOODS_FILE)
    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(
    foods,
    CALORIES_MIN,
    CALORIES_MAX,
    PROTEIN_MIN,
    PROTEIN_MAX,
    FAT_MIN,
    FAT_MAX,
)
    print_results(
    model,
    foods,
    food_vars,
    total_cost,
    total_calories,
    total_protein,
    total_fat,
    CALORIES_MIN,
    CALORIES_MAX,
    PROTEIN_MIN,
    PROTEIN_MAX,
    FAT_MIN,
    FAT_MAX,
)


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Error: {error}")
    