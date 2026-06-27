import pytest

from validation import validate_settings


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