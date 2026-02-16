import pandas as pd
import json
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse

# Load and process data
def load_data():
    df = pd.read_csv('finance_data.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['month'] = df['timestamp'].dt.to_period('M')
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['category'] = df['description'].apply(lambda x: 
        'Income' if any(cat in x for cat in ['Salary', 'Freelance', 'Dividend', 'Interest', 'Stock', 'Rental', 'Consulting', 'Bonus']) else
        'Shopping' if any(cat in x for cat in ['Amazon', 'Electronics', 'Grocery Store', 'Clothing', 'Home Improvement', 'Books', 'Pet', 'Health & Beauty']) else
        'Food & Dining' if any(cat in x for cat in ['Restaurant', 'Coffee', 'Fast Food', 'Groceries', 'Food Delivery', 'Takeout']) else
        'Transportation' if any(cat in x for cat in ['Gas Station', 'Uber', 'Lyft', 'Car Insurance', 'Car Maintenance', 'Parking', 'Toll', 'Public Transit']) else
        'Entertainment' if any(cat in x for cat in ['Netflix', 'Spotify', 'Movie', 'Concert', 'Gaming', 'Sports', 'Hobby', 'Streaming']) else
        'Bills & Utilities' if any(cat in x for cat in ['Electric', 'Water', 'Internet', 'Phone', 'Insurance Premium', 'Rent', 'Mortgage', 'Property Tax']) else
        'Healthcare' if any(cat in x for cat in ['Doctor', 'Pharmacy', 'Dental', 'Vision', 'Medical Test', 'Therapy', 'Gym']) else
        'Travel' if any(cat in x for cat in ['Flight', 'Hotel', 'Airbnb', 'Car Rental', 'Travel Insurance', 'Tour']) else
        'Other'
    )
    return df

def index(request):
    df = load_data()
    
    # Summary stats
    total_income = df[df['amount'] > 0]['amount'].sum()
    total_expenses = abs(df[df['amount'] < 0]['amount'].sum())
    net = total_income - total_expenses
    
    # Monthly data
    monthly = df.groupby('month').agg({
        'amount': 'sum'
    }).reset_index()
    monthly['month_str'] = monthly['month'].astype(str)
    
    # Category breakdown
    expenses_only = df[df['amount'] < 0].copy()
    category_totals = expenses_only.groupby('category')['amount'].sum().abs()
    category_data = [{'category': cat, 'amount': round(amt, 2)} for cat, amt in category_totals.items()]
    
    # Daily spending pattern
    daily_avg = df[df['amount'] < 0].groupby('day_of_week')['amount'].mean()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    daily_data = [{'day': day, 'avg': round(daily_avg.get(day, 0), 2)} for day in day_order]
    
    # Top transactions
    top_expenses = df[df['amount'] < 0].nsmallest(10, 'amount')[['timestamp', 'description', 'amount']].to_dict('records')
    for t in top_expenses:
        t['amount'] = abs(t['amount'])
        t['timestamp'] = t['timestamp'].strftime('%Y-%m-%d')
    
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
    }
    
    return render(request, 'dashboard/index.html', context)
