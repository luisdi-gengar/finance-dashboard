# Finance Dashboard

A Django-based finance dashboard with interactive charts using Plotly. Built with synthetic transaction data for demonstration purposes.

![Dashboard Preview](https://via.placeholder.com/800x400?text=Finance+Dashboard)

## Features

- **Interactive Charts** - Monthly cash flow, expense categories, daily spending patterns
- **Data Processing** - Pandas-powered data transformation and categorization
- **Modern UI** - Dark theme inspired by Twitter/X design
- **Responsive** - Works on desktop and mobile

## Tech Stack

- **Backend**: Django 6.0
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Plotly
- **Python**: 3.12+

## Project Structure

```
finance-dashboard/
├── finance_data.csv          # Synthetic transaction data
├── generate_data.py          # Script to generate new data
├── manage.py                 # Django management script
├── dashboard/
│   ├── views.py              # Main dashboard logic
│   ├── urls.py               # URL routing
│   └── templates/
│       └── dashboard/
│           └── index.html    # Frontend with Plotly charts
└── financeproject/
    ├── settings.py           # Django settings
    └── urls.py               # Project URLs
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

## Setup Instructions

### Prerequisites

- Python 3.12+
- uv (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/luisdi-gengar/finance-dashboard.git
   cd finance-dashboard
   ```

2. **Create virtual environment**
   ```bash
   # Using uv (recommended)
   uv venv .
   
   # Or using venv
   python3 -m venv .
   ```

3. **Activate virtual environment**
   ```bash
   # Linux/Mac
   source bin/activate
   
   # Windows
   Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install pandas matplotlib plotly django
   ```

5. **Run the server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://localhost:8000
   ```

### Regenerate Data

To generate new synthetic data:
```bash
python generate_data.py
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
