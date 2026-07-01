from optimization_model import build_and_solve_model
from result_builder import build_result


def test_build_result_returns_structured_optimal_result():
    foods = [
        {
            "name": "rice",
            "price_per_kg": 20,
            "kcal_per_100g": 360,
            "protein_per_100g": 7,
            "fat_per_100g": 1,
            "min_grams_per_day": 0,
            "max_grams_per_day": 1000,
        },
        {
            "name": "chicken",
            "price_per_kg": 100,
            "kcal_per_100g": 110,
            "protein_per_100g": 23,
            "fat_per_100g": 2,
            "min_grams_per_day": 0,
            "max_grams_per_day": 1000,
        },
        {
            "name": "oil",
            "price_per_kg": 90,
            "kcal_per_100g": 884,
            "protein_per_100g": 0,
            "fat_per_100g": 100,
            "min_grams_per_day": 0,
            "max_grams_per_day": 100,
        },
    ]

    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(
        foods,
        calories_min=2000,
        calories_max=2100,
        protein_min=100,
        protein_max=140,
        fat_min=40,
        fat_max=80,
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

    assert result["status"] == "Optimal"
    assert len(result["selected_foods"]) > 0
    assert result["totals"]["cost"] > 0
    assert 2000 <= result["totals"]["calories"] <= 2100
    assert 100 <= result["totals"]["protein"] <= 140
    assert 40 <= result["totals"]["fat"] <= 80


def test_build_result_returns_status_for_infeasible_model():
    foods = [
        {
            "name": "rice",
            "price_per_kg": 20,
            "kcal_per_100g": 360,
            "protein_per_100g": 7,
            "fat_per_100g": 1,
            "min_grams_per_day": 0,
            "max_grams_per_day": 100,
        }
    ]

    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(
        foods,
        calories_min=10000,
        calories_max=10100,
        protein_min=100,
        protein_max=120,
        fat_min=40,
        fat_max=60,
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

    assert result["status"] == "Infeasible"
    assert result["selected_foods"] == []
    assert result["totals"] is None