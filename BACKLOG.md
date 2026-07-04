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

* Done: Add more manually entered foods to `foods.csv`.
* Done: Add potatoes, dry pasta, dry lentils, canned tuna, and apple to the example dataset.
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

Planned scope:

* Done: Create a structured result representation for optimization results.
* Done: Separate result calculation from terminal printing.
* Done: Keep `result_printer.py` focused only on formatting and printing.
* Done: Add tests for result totals and selected food amounts.
* Done: Avoid changing the optimization model unless necessary.
* Done: Avoid adding new nutrition features in this version.

Purpose:

This version should make the project easier to test and easier to extend later. A structured result object or dictionary will make it possible to reuse optimization results outside the terminal, such as in a future web app, API, or report.

Out of scope:

* new foods
* micronutrients
* meal planning
* web app
* database
* API
* price scraping
* product matching

## v0.5.0 - Basic result export

Planned scope:

Completed:

* Done: Export structured optimization results to a JSON file.
* Done: Create a small `result_exporter.py` module.
* Done: Keep terminal output unchanged.
* Done: Add tests for JSON result export.
* Done: Format exported numeric values for readability.
* Done: Ignore generated `result.json` in Git.
* Done: Document JSON result export in README.
* Done: Avoid adding a database, web app, or API in this version.
* Done: Avoid changing the optimization model unless necessary.

Purpose:

This version should make optimization results reusable outside the terminal. Exporting results to JSON creates a simple foundation for future reports, APIs, dashboards, or web interfaces.

Out of scope:

* database
* web app
* API
* dashboards
* PDF export
* Excel export
* automatic price collection
* product matching

## v0.6.0 - Better infeasibility feedback

Planned scope:

* Add clearer feedback when the optimization model is infeasible.
* Show basic constraint ranges used in the failed run.
* Suggest practical next actions such as widening calorie ranges, increasing food max limits, or adding more foods.
* Keep the optimization model unchanged unless necessary.
* Keep terminal output simple and beginner-readable.
* Add tests for infeasible result printing or formatting.
* Avoid adding new nutrition features in this version.
* Avoid adding a database, web app, API, dashboard, or scraping.

Purpose:

This version should make failed optimization runs easier to understand. Instead of only reporting that no feasible solution exists, the program should help the user identify likely causes and reasonable next steps.

Out of scope:

* automatic diagnosis of exact infeasibility causes
* meal planning
* micronutrients
* database
* web app
* API
* dashboards
* price scraping
* product matching

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
