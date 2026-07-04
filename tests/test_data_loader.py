import pytest

from data_loader import load_foods, load_settings


def test_load_settings_reads_valid_json(tmp_path):
    settings_file = tmp_path / "settings.json"

    settings_file.write_text(
        """
        {
          "bodyweight_kg": 64.33,
          "calories_min": 2700,
          "calories_max": 2750,
          "protein_min_per_lb": 0.8,
          "protein_max_per_lb": 1.0,
          "fat_min_per_lb": 0.3,
          "fat_max_per_lb": 0.5
        }
        """,
        encoding="utf-8",
    )

    settings = load_settings(settings_file)

    assert settings["bodyweight_kg"] == 64.33
    assert settings["calories_min"] == 2700
    assert settings["calories_max"] == 2750


def test_load_settings_rejects_missing_file(tmp_path):
    missing_file = tmp_path / "missing_settings.json"

    with pytest.raises(ValueError, match="Settings file not found"):
        load_settings(missing_file)


def test_load_foods_reads_valid_csv(tmp_path):
    foods_file = tmp_path / "foods.csv"

    foods_file.write_text(
        "name,category,price_per_kg,kcal_per_100g,protein_per_100g,fat_per_100g,min_grams_per_day,max_grams_per_day\n"
        "rice,carb,20,360,7,1,0,500\n",
        encoding="utf-8",
    )

    foods = load_foods(foods_file)

    assert len(foods) == 1
    assert foods[0]["name"] == "rice"
    assert foods[0]["category"] == "carb"    
    assert foods[0]["price_per_kg"] == 20
    assert foods[0]["kcal_per_100g"] == 360
    assert foods[0]["protein_per_100g"] == 7
    assert foods[0]["fat_per_100g"] == 1
    assert foods[0]["min_grams_per_day"] == 0    
    assert foods[0]["max_grams_per_day"] == 500