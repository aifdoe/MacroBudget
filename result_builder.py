import pulp

from nutrition_warnings import build_nutrition_warnings


def build_result(model, foods, food_vars, total_cost, total_calories, total_protein, total_fat):
    status = pulp.LpStatus[model.status]

    result = {
        "status": status,
        "selected_foods": [],
        "totals": None,
        "warnings": [],
    }

    if status != "Optimal":
        return result

    selected_foods = []
    total_carbs = 0
    total_fiber = 0

    for food in foods:
        food_name = food["name"]
        grams = food_vars[food_name].value()

        if grams is not None and grams > 0.01:
            selected_foods.append(
                {
                    "name": food_name,
                    "grams": grams,
                    "cost": grams * food["price_per_kg"] / 1000,
                }
            )

            total_carbs += grams * food["carbs_per_100g"] / 100
            total_fiber += grams * food["fiber_per_100g"] / 100

    totals = {
        "cost": pulp.value(total_cost),
        "calories": pulp.value(total_calories),
        "protein": pulp.value(total_protein),
        "fat": pulp.value(total_fat),
        "carbs": total_carbs,
        "fiber": total_fiber,
    }

    result["selected_foods"] = selected_foods
    result["totals"] = totals
    result["warnings"] = build_nutrition_warnings(totals)

    return result