# MacroBudget

MacroBudget is a Python project that uses mathematical optimization to find low-cost food combinations that satisfy caloric, protein, and fat constraints.

The long-term goal is to build a practical food cost and nutrition optimizer for people who want to meet nutrition targets while minimizing food costs.

## Current version

This is an early local prototype.

The current version:

* reads food data from a CSV file
* models food amounts as decision variables
* minimizes total daily food cost
* enforces caloric, protein, and fat constraints
* supports maximum grams per day for each food
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
basmati_rice_dry: 338.1 g
oats: 300.0 g
eggs: 158.4 g
whey_protein: 38.7 g

Total cost: 36.14 SEK/day
Total calories: 2700 kcal
Total protein: 113.5 g
Total fat: 42.5 g
```

## Project structure

```text
macrobudget/
├── foods.csv
├── optimizer.py
├── requirements.txt
├── README.md
└── .gitignore
```

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

## Data

The current food data is stored manually in `foods.csv`.

The dataset is intentionally small and approximate in this version. The purpose of the current version is to prove that the optimization core works before adding larger food databases or product-level data.

Future versions may use official food composition data from Livsmedelsverket.

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
