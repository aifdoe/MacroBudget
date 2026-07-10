from pathlib import Path

from data_loader import load_foods, load_settings


def test_example_settings_file_is_valid():
    settings = load_settings(Path("example_settings.json"))

    assert settings["bodyweight_kg"] > 0
    assert settings["calories_min"] < settings["calories_max"]
    assert settings["protein_min_per_lb"] < settings["protein_max_per_lb"]
    assert settings["fat_min_per_lb"] < settings["fat_max_per_lb"]


def test_example_foods_file_is_valid():
    foods = load_foods(Path("example_foods.csv"))

    assert len(foods) > 0
    assert foods[0]["name"] == "basmati_rice_dry"
    assert foods[0]["category"] == "carb"