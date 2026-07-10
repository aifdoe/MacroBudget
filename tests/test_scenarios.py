from pathlib import Path

from data_loader import load_foods, load_settings
from optimization_model import build_and_solve_model
from optimizer import calculate_targets
from result_builder import build_result


def solve_scenario(settings_path, foods_path):
    settings = load_settings(settings_path)
    foods = load_foods(foods_path)
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

    return build_result(
        model,
        foods,
        food_vars,
        total_cost,
        total_calories,
        total_protein,
        total_fat,
    )


def test_optimal_scenario_solves_successfully():
    result = solve_scenario(
        Path("scenarios/optimal_settings.json"),
        Path("scenarios/optimal_foods.csv"),
    )

    assert result["status"] == "Optimal"
    assert len(result["selected_foods"]) > 0
    assert result["totals"] is not None


def test_infeasible_scenario_reports_infeasible():
    result = solve_scenario(
        Path("scenarios/infeasible_settings.json"),
        Path("scenarios/infeasible_foods.csv"),
    )

    assert result["status"] == "Infeasible"
    assert result["selected_foods"] == []
    assert result["totals"] is None