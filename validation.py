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