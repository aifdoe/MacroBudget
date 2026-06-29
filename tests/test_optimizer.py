import pytest

from optimizer import calculate_targets


def test_calculate_targets_converts_bodyweight_and_macro_ranges():
    settings = {
        "bodyweight_kg": 64.33,
        "calories_min": 2700,
        "calories_max": 2750,
        "protein_min_per_lb": 0.8,
        "protein_max_per_lb": 1.0,
        "fat_min_per_lb": 0.3,
        "fat_max_per_lb": 0.5,
    }

    targets = calculate_targets(settings)

    bodyweight_lb = 64.33 * 2.20462

    assert targets["calories_min"] == 2700
    assert targets["calories_max"] == 2750
    assert targets["protein_min"] == pytest.approx(0.8 * bodyweight_lb)
    assert targets["protein_max"] == pytest.approx(1.0 * bodyweight_lb)
    assert targets["fat_min"] == pytest.approx(0.3 * bodyweight_lb)
    assert targets["fat_max"] == pytest.approx(0.5 * bodyweight_lb)