### REVIEW TECH STACK - MIGRATE TO JAVA OR GO
next task

# Arcane Market

This is a lightweight Flask storefront for a fantasy universe. It simulates a virtual e-commerce experience where players can browse magical items such as swords, capes, relics, and armor, then complete a mock purchase transaction.

## Features

- Fantasy-themed catalog with item rarity and stock
- Simulated purchase endpoint for transactional flow
- Responsive storefront UI with order summary panel
- Python/Flask app structure ready to extend for a full game shop

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Then open http://127.0.0.1:5000/

## Example purchase simulation

The app exposes a POST endpoint at `/api/purchase` that accepts JSON like:

```json
{
  "item_id": 1,
  "quantity": 2
}
```

The response contains a simulated receipt and totals in gold.


## To do
Implement new version.

## Project structure

```text
ShoPlay/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   ├── script.js
│   │   └── styles.css
│   └── templates/
│       └── catalog.html
├── requirements.txt
├── run.py
├── pytest.ini
└── README.md
```
