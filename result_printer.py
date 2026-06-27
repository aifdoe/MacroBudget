import pulp


def print_results(
    model,
    foods,
    food_vars,
    total_cost,
    total_calories,
    total_protein,
    total_fat,
    calories_min,
    calories_max,
    protein_min,
    protein_max,
    fat_min,
    fat_max,
):
    status = pulp.LpStatus[model.status]

    print("Status:", status)
    print()

    print("Targets:")
    print(f"Calories: {calories_min:.0f}-{calories_max:.0f} kcal")
    print(f"Protein: {protein_min:.1f}-{protein_max:.1f} g")
    print(f"Fat: {fat_min:.1f}-{fat_max:.1f} g")
    print()

    if status == "Infeasible":
        print("No feasible solution found.")
        print("The current food list and constraints cannot satisfy the selected targets.")
        print("Try widening the calorie or macronutrient ranges, increasing food max limits, or adding more foods.")
        return

    if status == "Unbounded":
        print("The model is unbounded.")
        print("This usually means the optimization problem is missing an important constraint.")
        return

    if status != "Optimal":
        print("No optimal solution found.")
        print("Solver status:", status)
        return

    print("Food amounts per day:")

    for food in foods:
        food_name = food["name"]
        variable = food_vars[food_name]
        grams = variable.value()

        if grams > 0.01:
            cost = grams * food["price_per_kg"] / 1000
            print(f"{food_name}: {grams:.1f} g ({cost:.2f} SEK)")

    print()
    print(f"Total cost: {pulp.value(total_cost):.2f} SEK/day")
    print(f"Total calories: {pulp.value(total_calories):.0f} kcal")
    print(f"Total protein: {pulp.value(total_protein):.1f} g")
    print(f"Total fat: {pulp.value(total_fat):.1f} g")
    