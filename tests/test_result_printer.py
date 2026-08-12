from result_printer import print_results


def test_print_results_gives_helpful_feedback_for_infeasible_result(capsys):
    result = {
        "status": "Infeasible",
        "selected_foods": [],
        "totals": None,
        "warnings": [],
    }

    targets = {
        "calories_min": 2700,
        "calories_max": 2750,
        "protein_min": 113.5,
        "protein_max": 141.8,
        "fat_min": 42.5,
        "fat_max": 70.9,
    }

    print_results(result, targets)

    output = capsys.readouterr().out

    assert "Status: Infeasible" in output
    assert "Calories: 2700-2750 kcal" in output
    assert "Protein: 113.5-141.8 g" in output
    assert "Fat: 42.5-70.9 g" in output
    assert "Likely causes:" in output
    assert "Suggested next steps:" in output
    assert "max_grams_per_day" in output
    assert "min_grams_per_day" in output

def test_print_results_warns_when_fiber_is_high(capsys):
    result = {
        "status": "Optimal",
        "selected_foods": [
            {
                "name": "oats",
                "grams": 300.0,
                "cost": 7.5,
            }
        ],
        "totals": {
            "cost": 27.34,
            "calories": 2700,
            "protein": 113.5,
            "fat": 42.5,
            "carbs": 442.1,
            "fiber": 62.0,
        },
        "warnings": [
            "Fiber is high at 62.0 g. This may be impractical for some users."
        ],
    }

    targets = {
        "calories_min": 2700,
        "calories_max": 2750,
        "protein_min": 113.5,
        "protein_max": 141.8,
        "fat_min": 42.5,
        "fat_max": 70.9,
    }

    print_results(result, targets)

    output = capsys.readouterr().out

    assert "Nutrition warnings:" in output
    assert "Fiber is high at 62.0 g" in output