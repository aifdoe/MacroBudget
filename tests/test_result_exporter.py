import json

from result_exporter import export_result_to_json, format_result_for_export


def test_format_result_for_export_rounds_numeric_values():
    result = {
        "status": "Optimal",
        "selected_foods": [
            {
                "name": "pasta_dry",
                "grams": 216.92462,
                "cost": 6.507738600000001,
            }
        ],
        "totals": {
            "cost": 27.3356536,
            "calories": 2700.0000164000003,
            "protein": 113.4585648,
            "fat": 42.5469616,
        },
    }

    formatted_result = format_result_for_export(result)

    assert formatted_result == {
        "status": "Optimal",
        "selected_foods": [
            {
                "name": "pasta_dry",
                "grams": 216.9,
                "cost": 6.51,
            }
        ],
        "totals": {
            "cost": 27.34,
            "calories": 2700,
            "protein": 113.5,
            "fat": 42.5,
        },
    }


def test_format_result_for_export_handles_non_optimal_result():
    result = {
        "status": "Infeasible",
        "selected_foods": [],
        "totals": None,
    }

    formatted_result = format_result_for_export(result)

    assert formatted_result == {
        "status": "Infeasible",
        "selected_foods": [],
        "totals": None,
    }


def test_export_result_to_json_writes_formatted_result_file(tmp_path):
    result = {
        "status": "Optimal",
        "selected_foods": [
            {
                "name": "oats",
                "grams": 300.04,
                "cost": 7.504,
            }
        ],
        "totals": {
            "cost": 27.335,
            "calories": 2700.0001,
            "protein": 113.458,
            "fat": 42.546,
        },
    }

    output_file = tmp_path / "result.json"

    export_result_to_json(result, output_file)

    loaded_result = json.loads(output_file.read_text(encoding="utf-8"))

    assert loaded_result == {
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
        },
    }