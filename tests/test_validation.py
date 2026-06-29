import pytest

from validation import (
    parse_non_negative_number,
    parse_positive_number,
    validate_foods,
    validate_settings,
)

def test_validate_settings_accepts_valid_settings():
    settings = {
        "bodyweight_kg": 64.33,
        "calories_min": 2700,
        "calories_max": 2750,
        "protein_min_per_lb": 0.8,
        "protein_max_per_lb": 1.0,
        "fat_min_per_lb": 0.3,
        "fat_max_per_lb": 0.5,
    }

    validate_settings(settings)


def test_validate_settings_rejects_invalid_calorie_range():
    settings = {
        "bodyweight_kg": 64.33,
        "calories_min": 3000,
        "calories_max": 2700,
        "protein_min_per_lb": 0.8,
        "protein_max_per_lb": 1.0,
        "fat_min_per_lb": 0.3,
        "fat_max_per_lb": 0.5,
    }

    with pytest.raises(ValueError, match="calories_min must be lower than calories_max"):
        validate_settings(settings)

def test_parse_non_negative_number_rejects_negative_value():
    with pytest.raises(ValueError, match="price_per_kg cannot be negative"):
        parse_non_negative_number("-1", "price_per_kg", 3)


def test_parse_positive_number_rejects_zero_value():
    with pytest.raises(ValueError, match="max_grams_per_day must be greater than 0"):
        parse_positive_number("0", "max_grams_per_day", 4)


def test_validate_foods_rejects_empty_food_list():
    with pytest.raises(ValueError, match="foods.csv must contain at least one food"):
        validate_foods([])


def test_validate_foods_rejects_duplicate_names():
    foods = [
        {"name": "oats"},
        {"name": "oats"},
    ]

    with pytest.raises(ValueError, match="Duplicate food name in foods.csv: oats"):
        validate_foods(foods)