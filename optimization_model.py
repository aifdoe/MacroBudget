import pulp


def build_and_solve_model(
    foods,
    calories_min,
    calories_max,
    protein_min,
    protein_max,
    fat_min,
    fat_max,
):
    model = pulp.LpProblem("MacroBudget", pulp.LpMinimize)

    food_vars = {}

    for food in foods:
        food_name = food["name"]

        food_vars[food_name] = pulp.LpVariable(
            name=f"grams_{food_name}",
            lowBound=food["min_grams_per_day"],
            upBound=food["max_grams_per_day"],
            cat="Continuous",
        )

    total_cost = pulp.lpSum(
        food_vars[food["name"]] * food["price_per_kg"] / 1000
        for food in foods
    )

    total_calories = pulp.lpSum(
        food_vars[food["name"]] * food["kcal_per_100g"] / 100
        for food in foods
    )

    total_protein = pulp.lpSum(
        food_vars[food["name"]] * food["protein_per_100g"] / 100
        for food in foods
    )

    total_fat = pulp.lpSum(
        food_vars[food["name"]] * food["fat_per_100g"] / 100
        for food in foods
    )

    model += total_cost

    model += total_calories >= calories_min
    model += total_calories <= calories_max

    model += total_protein >= protein_min
    model += total_protein <= protein_max

    model += total_fat >= fat_min
    model += total_fat <= fat_max

    model.solve(pulp.PULP_CBC_CMD(msg=False))

    return model, food_vars, total_cost, total_calories, total_protein, total_fat
