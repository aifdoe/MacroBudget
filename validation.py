def validate_settings(settings):
    required_fields = [
        "bodyweight_kg",
        "calories_min",
        "calories_max",
        "protein_min_per_lb",
        "protein_max_per_lb",
        "fat_min_per_lb",
        "fat_max_per_lb",
    ]

    for field in required_fields:
        if field not in settings:
            raise ValueError(f"Missing required setting: {field}")

    for field in required_fields:
        value = settings[field]

        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"Setting must be a number: {field}")

    if settings["bodyweight_kg"] <= 0:
        raise ValueError("bodyweight_kg must be greater than 0")

    if settings["calories_min"] <= 0:
        raise ValueError("calories_min must be greater than 0")

    if settings["calories_max"] <= 0:
        raise ValueError("calories_max must be greater than 0")

    if settings["calories_min"] >= settings["calories_max"]:
        raise ValueError("calories_min must be lower than calories_max")

    if settings["protein_min_per_lb"] <= 0:
        raise ValueError("protein_min_per_lb must be greater than 0")

    if settings["protein_max_per_lb"] <= 0:
        raise ValueError("protein_max_per_lb must be greater than 0")

    if settings["protein_min_per_lb"] >= settings["protein_max_per_lb"]:
        raise ValueError("protein_min_per_lb must be lower than protein_max_per_lb")

    if settings["fat_min_per_lb"] <= 0:
        raise ValueError("fat_min_per_lb must be greater than 0")

    if settings["fat_max_per_lb"] <= 0:
        raise ValueError("fat_max_per_lb must be greater than 0")

    if settings["fat_min_per_lb"] >= settings["fat_max_per_lb"]:
        raise ValueError("fat_min_per_lb must be lower than fat_max_per_lb")
    
def validate_food_columns(fieldnames):
    required_columns = [
        "name",
        "price_per_kg",
        "kcal_per_100g",
        "protein_per_100g",
        "fat_per_100g",
        "max_grams_per_day",
    ]

    if fieldnames is None:
        raise ValueError("foods.csv is empty")

    for column in required_columns:
        if column not in fieldnames:
            raise ValueError(f"foods.csv is missing required column: {column}")


def parse_food_name(value, row_number):
    name = value.strip()

    if name == "":
        raise ValueError(f"foods.csv row {row_number}: name cannot be empty")

    return name


def parse_non_negative_number(value, field_name, row_number):
    try:
        number = float(value)
    except ValueError:
        raise ValueError(f"foods.csv row {row_number}: {field_name} must be a number")

    if number < 0:
        raise ValueError(f"foods.csv row {row_number}: {field_name} cannot be negative")

    return number


def parse_positive_number(value, field_name, row_number):
    number = parse_non_negative_number(value, field_name, row_number)

    if number <= 0:
        raise ValueError(f"foods.csv row {row_number}: {field_name} must be greater than 0")

    return number


def validate_foods(foods):
    if len(foods) == 0:
        raise ValueError("foods.csv must contain at least one food")

    seen_names = set()

    for food in foods:
        food_name = food["name"]

        if food_name in seen_names:
            raise ValueError(f"Duplicate food name in foods.csv: {food_name}")

        seen_names.add(food_name)