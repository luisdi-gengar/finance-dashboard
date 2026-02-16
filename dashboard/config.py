"""
Configuration for finance dashboard categories and translations.
Shared between Python (views) and JavaScript (frontend).
"""

# Category definitions with keywords and colors
CATEGORIES = {
    'Income': {
        'keywords': ['Salary', 'Freelance', 'Dividend', 'Interest', 'Stock', 'Rental', 'Consulting', 'Bonus'],
        'color': '#00ba7c',
    },
    'Shopping': {
        'keywords': ['Amazon', 'Electronics', 'Grocery Store', 'Clothing', 'Home Improvement', 'Books', 'Pet', 'Health & Beauty'],
        'color': '#f4212e',
    },
    'Food & Dining': {
        'keywords': ['Restaurant', 'Coffee', 'Fast Food', 'Groceries', 'Food Delivery', 'Takeout'],
        'color': '#ff7a1a',
    },
    'Transportation': {
        'keywords': ['Gas Station', 'Uber', 'Lyft', 'Car Insurance', 'Car Maintenance', 'Parking', 'Toll', 'Public Transit'],
        'color': '#ffd400',
    },
    'Entertainment': {
        'keywords': ['Netflix', 'Spotify', 'Movie', 'Concert', 'Gaming', 'Sports', 'Hobby', 'Streaming'],
        'color': '#00ba7c',
    },
    'Bills & Utilities': {
        'keywords': ['Electric', 'Water', 'Internet', 'Phone', 'Insurance Premium', 'Rent', 'Mortgage', 'Property Tax'],
        'color': '#1d9bf0',
    },
    'Healthcare': {
        'keywords': ['Doctor', 'Pharmacy', 'Dental', 'Vision', 'Medical Test', 'Therapy', 'Gym'],
        'color': '#9d36d6',
    },
    'Travel': {
        'keywords': ['Flight', 'Hotel', 'Airbnb', 'Car Rental', 'Travel Insurance', 'Tour'],
        'color': '#e0245e',
    },
}

# Translations for labels
TRANSLATIONS = {
    'en': {
        'income': '💵 Income',
        'expenses': '💸 Expenses',
        'net': '📊 Net',
        'monthly_cash_flow': '📈 Monthly Cash Flow',
        'expenses_by_category': '🗂️ Expenses',
        'daily_average': '📅 Daily Avg',
        'top_expenses': '💸 Top Expenses',
        'date': 'Date',
        'description': 'Description',
        'amount': 'Amount',
        'transactions': 'transactions',
    },
    'es': {
        'income': '💵 Ingresos',
        'expenses': '💸 Gastos',
        'net': '📊 Neto',
        'monthly_cash_flow': '📈 Flujo de Caja Mensual',
        'expenses_by_category': '🗂️ Gastos',
        'daily_average': '📅 Promedio Diario',
        'top_expenses': '💸 Principales Gastos',
        'date': 'Fecha',
        'description': 'Descripción',
        'amount': 'Monto',
        'transactions': 'transacciones',
    },
}

# Category translations
CATEGORY_TRANSLATIONS = {
    'en': {
        'Shopping': 'Shopping',
        'Food & Dining': 'Food & Dining',
        'Transportation': 'Transport',
        'Entertainment': 'Entertainment',
        'Bills & Utilities': 'Bills',
        'Healthcare': 'Healthcare',
        'Travel': 'Travel',
        'Other': 'Other',
    },
    'es': {
        'Shopping': 'Compras',
        'Food & Dining': 'Comida',
        'Transportation': 'Transporte',
        'Entertainment': 'Entretenim.',
        'Bills & Utilities': 'Facturas',
        'Healthcare': 'Salud',
        'Travel': 'Viajes',
        'Other': 'Otros',
    },
}


def categorize_transaction(description):
    """Categorize a transaction based on its description."""
    for category, config in CATEGORIES.items():
        for keyword in config['keywords']:
            if keyword.lower() in description.lower():
                return category
    return 'Other'


def get_category_color(category):
    """Get color for a category."""
    return CATEGORIES.get(category, {}).get('color', '#71767b')


def get_all_categories():
    """Return list of all category names."""
    return list(CATEGORIES.keys()) + ['Other']
