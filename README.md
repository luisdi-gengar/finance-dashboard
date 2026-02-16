# Finance Dashboard

A Django-based finance dashboard with interactive charts using Plotly. Built with synthetic transaction data for demonstration purposes.

## Features

- **Interactive Charts** - Monthly cash flow, expense categories, daily spending patterns
- **Data Processing** - Pandas-powered data transformation and categorization
- **Modern UI** - Dark theme inspired by Twitter/X design
- **Responsive** - Works on desktop and mobile

## Tech Stack

- **Backend**: Django 6.0
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Plotly
- **Package Manager**: UV
- **Python**: 3.12+

## Quick Start

```bash
# Clone and enter directory
git clone https://github.com/luisdi-gengar/finance-dashboard.git
cd finance-dashboard

# Install dependencies with UV
uv sync

# Run the server
uv run python manage.py runserver
```

Open http://localhost:8000 to view the dashboard.

## Project Structure

```
finance-dashboard/
├── pyproject.toml           # UV project configuration
├── finance_data.csv        # Synthetic transaction data
├── generate_data.py        # Script to generate new data
├── manage.py               # Django management script
├── dashboard/
│   ├── views.py            # Main dashboard logic
│   ├── urls.py             # URL routing
│   └── templates/
│       └── dashboard/
│           └── index.html  # Frontend with Plotly charts
└── financeproject/
    ├── settings.py         # Django settings
    └── urls.py             # Project URLs
```

## Logic Explanation

### 1. Data Generation (`generate_data.py`)

Creates 500 synthetic transactions with:
- **timestamp**: Random datetime over the past year
- **description**: Category-specific transaction descriptions
- **amount**: Positive for income, negative for expenses

Categories:
| Category | Examples |
|----------|----------|
| Income | Salary, Freelance, Dividends, Interest |
| Shopping | Amazon, Electronics, Groceries |
| Food & Dining | Restaurants, Coffee, Delivery |
| Transportation | Gas, Uber, Insurance |
| Entertainment | Netflix, Concerts, Gaming |
| Bills & Utilities | Rent, Electric, Internet |
| Healthcare | Doctor, Pharmacy, Gym |
| Travel | Flights, Hotels, Airbnb |

### 2. Data Processing (`views.py`)

When the dashboard loads:
1. Load CSV into Pandas DataFrame
2. Parse timestamps and extract month/day info
3. Categorize transactions based on description keywords
4. Calculate aggregates:
   - Total income/expenses/net
   - Monthly cash flow
   - Category breakdown
   - Average daily spending by weekday

### 3. Visualization (`index.html`)

Three interactive Plotly charts:
- **Line Chart**: Monthly cash flow over time
- **Pie Chart**: Expense distribution by category
- **Bar Chart**: Average spending by day of week

## UV Commands

```bash
# Install dependencies
uv sync

# Add a new dependency
uv add django

# Remove a dependency
uv remove django

# Run Django commands
uv run python manage.py migrate
uv run python manage.py createsuperuser

# Run the development server
uv run python manage.py runserver

# Regenerate synthetic data
uv run python generate_data.py

# Shell (Django shell)
uv run python manage.py shell
```

## Regenerate Data

To generate new synthetic data:
```bash
uv run python generate_data.py
```

This creates a fresh `finance_data.csv` with 500 new transactions.

## Customization

### Add Real Data

Replace `finance_data.csv` with your own data. Required columns:
- `timestamp` - Date/time of transaction
- `description` - Transaction description
- `amount` - USD amount (positive = income, negative = expense)

### Modify Categories

Edit the `categories` dictionary in `generate_data.py` to add custom categories.

### Change Chart Colors

Edit the Plotly trace configurations in `dashboard/templates/dashboard/index.html`.

## License

MIT License - Feel free to use and modify!

---

Built with Django + Plotly 💰📊
