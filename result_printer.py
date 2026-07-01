def print_results(result, targets):
    status = result["status"]

    print("Status:", status)
    print()

    print("Targets:")
    print(f"Calories: {targets['calories_min']:.0f}-{targets['calories_max']:.0f} kcal")
    print(f"Protein: {targets['protein_min']:.1f}-{targets['protein_max']:.1f} g")
    print(f"Fat: {targets['fat_min']:.1f}-{targets['fat_max']:.1f} g")
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

    for food in result["selected_foods"]:
        print(f"{food['name']}: {food['grams']:.1f} g ({food['cost']:.2f} SEK)")

    totals = result["totals"]

    print()
    print(f"Total cost: {totals['cost']:.2f} SEK/day")
    print(f"Total calories: {totals['calories']:.0f} kcal")
    print(f"Total protein: {totals['protein']:.1f} g")
    print(f"Total fat: {totals['fat']:.1f} g")