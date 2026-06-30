# Changelog

All notable changes to MacroBudget will be documented in this file.

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
