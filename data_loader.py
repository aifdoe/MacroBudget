import csv
import json

from validation import (
    parse_food_name,
    parse_non_negative_number,
    parse_positive_number,
    validate_food_columns,
    validate_foods,
    validate_settings,
)


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


def load_foods(file_path):
    foods = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            validate_food_columns(reader.fieldnames)

            for row_number, row in enumerate(reader, start=2):
                food = {
                    "name": parse_food_name(row["name"], row_number),
                    "price_per_kg": parse_non_negative_number(
                        row["price_per_kg"], "price_per_kg", row_number
                    ),
                    "kcal_per_100g": parse_non_negative_number(
                        row["kcal_per_100g"], "kcal_per_100g", row_number
                    ),
                    "protein_per_100g": parse_non_negative_number(
                        row["protein_per_100g"], "protein_per_100g", row_number
                    ),
                    "fat_per_100g": parse_non_negative_number(
                        row["fat_per_100g"], "fat_per_100g", row_number
                    ),
                    "min_grams_per_day": parse_non_negative_number(
                        row["min_grams_per_day"], "min_grams_per_day", row_number
                    ),                    
                    "max_grams_per_day": parse_positive_number(
                        row["max_grams_per_day"], "max_grams_per_day", row_number
                    ),
                }

                foods.append(food)

    except FileNotFoundError:
        raise ValueError(f"Foods file not found: {file_path}")

    validate_foods(foods)

    return foods
