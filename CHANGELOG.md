# Changelog

All notable changes to MacroBudget will be documented in this file.

## v0.2.0 - Practical food constraints

### Added

* Added `min_grams_per_day` to `foods.csv`.
* Updated food data loading to read minimum grams per food.
* Updated validation to reject foods where `min_grams_per_day` is greater than `max_grams_per_day`.
* Updated the optimization model to use minimum grams as the lower bound for each food variable.
* Added tests for minimum gram constraints.
* Added a minimum daily amount of frozen vegetables to the example food dataset.
* Updated README example output to show the practical vegetable constraint.

### Notes

This version makes the optimizer slightly more practical while keeping the model simple and local.

## v0.1.0 - Initial optimization core

### Added

* Built a local Python-based food cost optimizer.
* Added CSV-based food data loading from `foods.csv`.
* Added JSON-based user target loading from `settings.json`.
* Implemented linear programming optimization with PuLP.
* Added calorie, protein, and fat constraints.
* Added maximum grams per day constraints for each food.
* Added user-friendly validation errors for settings and food data.
* Added infeasible model handling.
* Split the project into separate modules for data loading, validation, optimization, and result printing.
* Added automated tests with pytest.
* Documented setup, usage, project structure, limitations, and roadmap in `README.md`.

### Notes

This version is a local prototype focused on proving the optimization core. It is not yet a complete diet planning tool.
