import pandas as pd
import json
import os
from functools import lru_cache
from django.shortcuts import render
from .config import CATEGORIES, categorize_transaction, get_category_color, TRANSLATIONS, CATEGORY_TRANSLATIONS


# Cache the data loading for better performance
@lru_cache(maxsize=1)
def load_data():
    """
    Load and process finance data from CSV.
    Cached to avoid re-reading on every request.
    """
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'finance_data.csv')
    
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None
    
    # Parse timestamps
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['month'] = df['timestamp'].dt.to_period('M')
    df['day_of_week'] = df['timestamp'].dt.day_name()
    
    # Categorize transactions using config
    df['category'] = df['description'].apply(categorize_transaction)
    
    return df


def index(request):
    df = load_data()
    
    # Handle data loading errors
    if df is None:
        return render(request, 'dashboard/error.html', {
            'error': 'Unable to load data. Please ensure finance_data.csv exists.'
        })
    
    # Summary stats
    total_income = df[df['amount'] > 0]['amount'].sum()
    total_expenses = abs(df[df['amount'] < 0]['amount'].sum())
    net = total_income - total_expenses
    
    # Monthly data
    monthly = df.groupby('month').agg({'amount': 'sum'}).reset_index()
    monthly['month_str'] = monthly['month'].astype(str)
    
    # Category breakdown (expenses only, exclude income)
    expenses_only = df[df['amount'] < 0].copy()
    category_totals = expenses_only.groupby('category')['amount'].sum().abs()
    # Filter out Income category from chart
    category_data = [
        {'category': cat, 'amount': round(amt, 2), 'color': get_category_color(cat)}
        for cat, amt in category_totals.items() if cat != 'Income'
    ]
    
    # Daily spending pattern
    daily_avg = df[df['amount'] < 0].groupby('day_of_week')['amount'].mean()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_data = [
        {'day': day, 'avg': round(daily_avg.get(day, 0), 2)} 
        for day in day_order
    ]
    
    # Top transactions
    top_expenses = df[df['amount'] < 0].nsmallest(10, 'amount')[
        ['timestamp', 'description', 'amount']
    ].to_dict('records')
    for t in top_expenses:
        t['amount'] = abs(t['amount'])
        t['timestamp'] = t['timestamp'].strftime('%Y-%m-%d')
    
    # Build context with translations
    context = {
        'total_income': round(total_income, 2),
        'total_expenses': round(total_expenses, 2),
        'net': round(net, 2),
        'monthly_labels': json.dumps([m for m in monthly['month_str']]),
        'monthly_data': json.dumps([round(a, 2) for a in monthly['amount']]),
        'category_data': json.dumps(category_data),
        'daily_data': json.dumps(daily_data),
        'top_expenses': top_expenses,
        'num_transactions': len(df),
        # Translations for template
        'translations': json.dumps(TRANSLATIONS),
        'category_labels': json.dumps(CATEGORY_TRANSLATIONS),
    }
    
    return render(request, 'dashboard/index.html', context)
