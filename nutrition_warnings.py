HIGH_FIBER_WARNING_THRESHOLD_GRAMS = 50


def build_nutrition_warnings(totals):
    warnings = []

    if totals["fiber"] > HIGH_FIBER_WARNING_THRESHOLD_GRAMS:
        warnings.append(
            f"Fiber is high at {totals['fiber']:.1f} g. "
            "This may be impractical for some users. "
            "Consider reviewing high-fiber foods or future fiber constraints."
        )

    return warnings