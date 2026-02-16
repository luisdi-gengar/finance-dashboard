"""Generate synthetic finance data"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Categories and descriptions
categories = {
    'Income': [
        'Salary - Monthly',
        'Freelance Project Payment',
        'Dividend Income',
        'Interest Earned',
        'Stock Sale Profit',
        'Rental Income',
        'Consulting Fee',
        'Bonus',
    ],
    'Shopping': [
        'Amazon Purchase',
        'Electronics - Laptop',
        'Grocery Store',
        'Clothing - Items',
        'Home Improvement',
        'Books & Media',
        'Pet Supplies',
        'Health & Beauty',
    ],
    'Food & Dining': [
        'Restaurant - Dinner',
        'Coffee Shop',
        'Fast Food',
        'Groceries - Whole Foods',
        'Groceries - Costco',
        'Food Delivery',
        'Takeout',
        'Groceries - Trader Joes',
    ],
    'Transportation': [
        'Gas Station',
        'Uber Ride',
        'Lyft Ride',
        'Car Insurance',
        'Car Maintenance',
        'Parking Fee',
        'Toll Road',
        'Public Transit',
    ],
    'Entertainment': [
        'Netflix Subscription',
        'Spotify Subscription',
        'Movie Theater',
        'Concert Tickets',
        'Gaming - Purchase',
        'Sports Event',
        'Hobby Supplies',
        'Streaming Services',
    ],
    'Bills & Utilities': [
        'Electric Bill',
        'Water Bill',
        'Internet Service',
        'Phone Bill',
        'Insurance Premium',
        'Rent Payment',
        'Mortgage Payment',
        'Property Tax',
    ],
    'Healthcare': [
        'Doctor Visit',
        'Pharmacy - Prescription',
        'Dental Checkup',
        'Vision Care',
        'Health Insurance',
        'Medical Test',
        'Therapy Session',
        'Gym Membership',
    ],
    'Travel': [
        'Flight Booking',
        'Hotel Stay',
        'Airbnb Rental',
        'Car Rental',
        'Travel Insurance',
        'Restaurant - Travel',
        'Souvenirs',
        'Tour Booking',
    ],
}

# Generate 500 transactions over the past year
n_transactions = 500
data = []

start_date = datetime.now() - timedelta(days=365)

for i in range(n_transactions):
    # Random timestamp
    days_offset = random.randint(0, 365)
    hours_offset = random.randint(0, 23)
    minutes_offset = random.randint(0, 59)
    timestamp = start_date + timedelta(days=days_offset, hours=hours_offset, minutes=minutes_offset)
    
    # Choose category and description
    category = random.choice(list(categories.keys()))
    description = random.choice(categories[category])
    
    # Generate amount based on category
    if category == 'Income':
        amount = random.uniform(500, 15000)
    elif category == 'Bills & Utilities':
        amount = random.uniform(50, 2500)
    elif category == 'Healthcare':
        amount = random.uniform(20, 1500)
    elif category == 'Travel':
        amount = random.uniform(100, 3000)
    elif category == 'Shopping':
        amount = random.uniform(10, 1500)
    elif category == 'Food & Dining':
        amount = random.uniform(5, 200)
    elif category == 'Transportation':
        amount = random.uniform(5, 300)
    else:  # Entertainment
        amount = random.uniform(5, 500)
    
    # Income is positive, expenses are negative
    if category == 'Income':
        amount = amount
    else:
        amount = -abs(amount)
    
    data.append({
        'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'description': description,
        'amount': round(amount, 2)
    })

# Create DataFrame and sort by date
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values('timestamp').reset_index(drop=True)

# Save to CSV
df.to_csv('finance_data.csv', index=False)
print(f"Generated {len(df)} transactions")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Total income: ${df[df['amount'] > 0]['amount'].sum():,.2f}")
print(f"Total expenses: ${abs(df[df['amount'] < 0]['amount'].sum()):,.2f}")
print(f"Net: ${df['amount'].sum():,.2f}")
print("\nFirst 10 rows:")
print(df.head(10))
print("\nData saved to finance_data.csv")
