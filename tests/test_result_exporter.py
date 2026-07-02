import json

from result_exporter import export_result_to_json


def test_export_result_to_json_writes_result_file(tmp_path):
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
        },
    }

    output_file = tmp_path / "result.json"

    export_result_to_json(result, output_file)

    loaded_result = json.loads(output_file.read_text(encoding="utf-8"))

    assert loaded_result == result