import pulp


def build_result(model, foods, food_vars, total_cost, total_calories, total_protein, total_fat):
    status = pulp.LpStatus[model.status]

    result = {
        "status": status,
        "selected_foods": [],
        "totals": None,
    }

    if status != "Optimal":
        return result

    selected_foods = []

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

    result["selected_foods"] = selected_foods
    result["totals"] = {
        "cost": pulp.value(total_cost),
        "calories": pulp.value(total_calories),
        "protein": pulp.value(total_protein),
        "fat": pulp.value(total_fat),
    }

    return result