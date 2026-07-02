import json


def format_result_for_export(result):
    formatted_result = {
        "status": result["status"],
        "selected_foods": [],
        "totals": None,
    }

    for food in result["selected_foods"]:
        formatted_result["selected_foods"].append(
            {
                "name": food["name"],
                "grams": round(food["grams"], 1),
                "cost": round(food["cost"], 2),
            }
        )

    if result["totals"] is not None:
        formatted_result["totals"] = {
            "cost": round(result["totals"]["cost"], 2),
            "calories": round(result["totals"]["calories"]),
            "protein": round(result["totals"]["protein"], 1),
            "fat": round(result["totals"]["fat"], 1),
        }

    return formatted_result


def export_result_to_json(result, file_path):
    formatted_result = format_result_for_export(result)

    with open(file_path, mode="w", encoding="utf-8") as file:
        json.dump(formatted_result, file, indent=2)
        file.write("\n")