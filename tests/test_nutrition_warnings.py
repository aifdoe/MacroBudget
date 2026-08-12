from nutrition_warnings import build_nutrition_warnings


def test_build_nutrition_warnings_returns_warning_for_high_fiber():
    totals = {
        "fiber": 62.0,
    }

    warnings = build_nutrition_warnings(totals)

    assert len(warnings) == 1
    assert "Fiber is high at 62.0 g" in warnings[0]


def test_build_nutrition_warnings_returns_no_warning_for_normal_fiber():
    totals = {
        "fiber": 30.0,
    }

    warnings = build_nutrition_warnings(totals)

    assert warnings == []