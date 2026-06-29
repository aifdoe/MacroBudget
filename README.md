# MacroBudget

MacroBudget is a Python project that uses mathematical optimization to find low-cost food combinations that satisfy caloric, protein, and fat constraints.

The long-term goal is to build a practical food cost and nutrition optimizer for people who want to meet nutrition targets while minimizing food costs.

## Current version

This is an early local prototype.

The current version:

* reads food data from a CSV file
* reads user targets from a settings file
* models food amounts as decision variables
* minimizes total daily food cost
* enforces caloric, protein, and fat constraints
* supports maximum grams per day for each food
* validates user settings and food data
* reports when no feasible solution exists
* prints an optimized daily food plan in grams

## Why this project exists

Food planning can be treated as an optimization problem.

Given a set of foods with prices and nutrition values, the system tries to answer:

> What is the cheapest combination of foods that satisfies the user's nutrition targets?

This is similar to a simplified operations research problem, where the goal is to minimize cost while respecting nutritional and practical constraints.

## Current model

The optimizer currently uses linear programming.

For each food, the model creates a decision variable:

```text
grams_of_food = how many grams of that food to eat per day
```

The objective function is:

```text
minimize total daily cost
```

The constraints include:

```text
calories between selected minimum and maximum
protein between selected minimum and maximum
fat between selected minimum and maximum
maximum grams per food per day
```

## Example output

```text
Status: Optimal

Targets:
Calories: 2700-2750 kcal
Protein: 113.5-141.8 g
Fat: 42.5-70.9 g

Food amounts per day:
basmati_rice_dry: 338.1 g (11.83 SEK)
oats: 300.0 g (7.50 SEK)
eggs: 158.4 g (7.13 SEK)
whey_protein: 38.7 g (9.68 SEK)

Total cost: 36.14 SEK/day
Total calories: 2700 kcal
Total protein: 113.5 g
Total fat: 42.5 g
```

## Project structure

```text
macrobudget/
|-- foods.csv
|-- settings.json
|-- optimizer.py
|-- data_loader.py
|-- validation.py
|-- optimization_model.py
|-- result_printer.py
|-- requirements.txt
|-- README.md
|-- .gitignore
`-- tests/
    |-- test_data_loader.py
    |-- test_optimization_model.py
    |-- test_optimizer.py
    `-- test_validation.py
```

Main responsibilities:

* `optimizer.py` runs the main program flow.
* `data_loader.py` reads `foods.csv` and `settings.json`.
* `validation.py` validates user settings and food data.
* `optimization_model.py` builds and solves the linear programming model.
* `result_printer.py` formats and prints terminal output.
* `tests/` contains automated tests for validation, data loading, target calculation, and optimization behavior.

## Requirements

* Python 3.13
* PuLP
* pytest for running tests

The required Python packages are listed in `requirements.txt`.

## How to run

Create and activate a virtual environment, then install the required packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the optimizer:

```powershell
python optimizer.py
```

## Tests

The project uses `pytest` for automated tests.

To run the test suite:

```bash
python -m pytest
```

Current tests cover user settings validation, food data validation, data loading, target calculation, optimization model constraints, and infeasible model behavior.

## Data

The current food data is stored manually in `foods.csv`.

The dataset is intentionally small and approximate in this version. The purpose of the current version is to prove that the optimization core works before adding larger food databases or product-level data.

Future versions may use official food composition data from Livsmedelsverket.

## User settings

User targets are stored in `settings.json`.

Example:

```json
{
  "bodyweight_kg": 64.33,
  "calories_min": 2700,
  "calories_max": 2750,
  "protein_min_per_lb": 0.8,
  "protein_max_per_lb": 1.0,
  "fat_min_per_lb": 0.3,
  "fat_max_per_lb": 0.5
}
```

The optimizer uses these settings to calculate the calorie, protein, and fat constraints.


## Limitations

This version is not a complete diet planning tool.

Current limitations:

* no micronutrients
* no meal structure
* no package sizes
* no inventory tracking
* no expiration dates
* no real product matching
* no automatic price collection
* no web app or user interface

Some optimized results may be mathematically valid but not yet practical as real diets.

## Roadmap

### Version 1: Optimization core

* local Python program
* small CSV food dataset
* calorie, protein, and fat constraints
* cost minimization
* basic practical max limits

### Version 2: Better nutrition model

* more foods
* micronutrient constraints
* fiber and sodium constraints
* better practical food limits

### Version 3: Real products

* product database
* package sizes
* integer optimization
* product-to-food matching

### Version 4: Inventory and time

* food inventory
* planning across multiple days or weeks
* expiration date handling
* reduced food waste

### Version 5: Product interface

* web app or app interface
* price collection
* AI-assisted product matching
* dashboards and visualizations

## Technical focus

This project is mainly focused on:

* Python
* linear programming
* mathematical optimization
* data modeling
* cost minimization
* practical nutrition constraints
