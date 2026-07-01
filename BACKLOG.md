# Backlog

This file tracks planned improvements for MacroBudget.

The goal is to keep development focused and avoid adding advanced product features before the optimization core is strong.

## v0.2.0 - Practical food constraints

Planned scope:

* Done: Add `min_grams_per_day` to `foods.csv`.
* Done: Update food data validation for minimum gram limits.
* Done: Update the optimization model to support both minimum and maximum grams per food.
* Done: Add tests for minimum gram constraints.
* Done: Update README documentation and example output if needed.
* Done: Require a minimum daily amount of frozen vegetables in the example food dataset.

Purpose:

This version should make the optimizer slightly more practical while still keeping the model simple and local.

Example use cases:

* require at least some vegetables
* require a minimum amount of a selected staple food
* avoid solutions that technically work but ignore practical food inclusion

## v0.3.0 - Improved food dataset

Planned scope:

* Add more manually entered foods to `foods.csv`.
* Keep the dataset small enough to review manually.
* Improve approximate price and nutrition values where obvious.
* Avoid adding micronutrients in this version.
* Avoid adding real product matching in this version.
* Run the optimizer after each dataset change to check how the solution changes.
* Update README example output if the optimized result changes significantly.

Purpose:

This version should make the optimizer work with a more realistic set of food options while keeping the model simple, local, and understandable.

Out of scope:

* micronutrients
* web scraping
* APIs
* databases
* product-level store matching
* package sizes
* integer optimization

## v0.4.0 - Cleaner result representation

Possible scope:

* Separate raw optimization result calculation from terminal printing.
* Create a structured result object or dictionary.
* Make result output easier to test.
* Add tests for total cost, calories, protein, and fat calculations.

## Later versions

Possible future work:

* micronutrient constraints
* fiber and sodium constraints
* package sizes
* integer optimization
* real product data
* inventory tracking
* multi-day planning
* web app or app interface
* price collection
* AI-assisted product matching

## Not now

These are intentionally out of scope for the current stage:

* web app
* database
* API
* web scraping
* dashboards
* automatic price collection
* real store product matching
* advanced meal planning
* user accounts
* mobile app

The current priority is to keep the project simple, understandable, tested, and technically solid.
