import pulp

from optimization_model import build_and_solve_model


def test_optimization_model_finds_solution_within_constraints():
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

    calories_min = 2000
    calories_max = 2100
    protein_min = 100
    protein_max = 140
    fat_min = 40
    fat_max = 80

    model, food_vars, total_cost, total_calories, total_protein, total_fat = build_and_solve_model(
        foods,
        calories_min,
        calories_max,
        protein_min,
        protein_max,
        fat_min,
        fat_max,
    )

    assert pulp.LpStatus[model.status] == "Optimal"
    assert calories_min <= pulp.value(total_calories) <= calories_max
    assert protein_min <= pulp.value(total_protein) <= protein_max
    assert fat_min <= pulp.value(total_fat) <= fat_max
    assert pulp.value(total_cost) > 0


def test_optimization_model_reports_infeasible_when_targets_are_impossible():
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

    assert pulp.LpStatus[model.status] == "Infeasible"

def test_optimization_model_respects_minimum_grams_constraint():
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
            "name": "vegetables",
            "price_per_kg": 30,
            "kcal_per_100g": 50,
            "protein_per_100g": 3,
            "fat_per_100g": 0.5,
            "min_grams_per_day": 100,
            "max_grams_per_day": 500,
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
        calories_max=2200,
        protein_min=90,
        protein_max=140,
        fat_min=40,
        fat_max=80,
    )

    assert pulp.LpStatus[model.status] == "Optimal"
    assert food_vars["vegetables"].value() >= 100