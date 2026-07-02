# Changelog

All notable changes to MacroBudget will be documented in this file.

## v0.5.0 - Basic result export

### Added

* Added `result_exporter.py` for exporting structured optimization results to JSON.
* Added `format_result_for_export()` to prepare readable user-facing export values.
* Added tests for JSON result export and export formatting.
* Added automatic `result.json` generation when running `python optimizer.py`.

### Changed

* Updated `optimizer.py` to export the structured result after optimization.
* Updated README to document JSON result export.
* Updated BACKLOG to mark the v0.5.0 result export scope as completed.

### Notes

This version adds a basic machine-readable output format while keeping the terminal output unchanged. The generated `result.json` file is ignored by Git because it is local program output, not source code.

The optimization model was not changed in this release.

## v0.4.0 - Cleaner result representation

### Added

* Added `result_builder.py` to convert PuLP optimization output into a structured Python result dictionary.
* Added tests for structured optimization results.
* Added result handling for infeasible models.

### Changed

* Updated `optimizer.py` to build a structured result before printing.
* Updated `result_printer.py` to print from structured result data instead of raw PuLP objects.
* Updated README project structure and module responsibilities.
* Updated backlog documentation for result representation work.

### Notes

This version improves internal architecture without changing the optimization model or user-facing output. The project is now easier to test and easier to extend toward future interfaces such as reports, APIs, or web apps.

## v0.3.0 - Improved food dataset

### Added

* Added more manually entered foods to `foods.csv`.
* Added potatoes, dry pasta, dry lentils, canned tuna, and apple to the example dataset.
* Updated README example output after the expanded dataset changed the optimized solution.
* Updated backlog documentation for the dataset improvement work.

### Notes

This version expands the small local dataset while keeping the project simple and manually reviewable. The food data is still approximate and intended for testing the optimization workflow, not for medical or dietary advice.

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
