"""
Django management command to generate synthetic finance data.
"""
import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
import pandas as pd


CATEGORIES = {
    'Income': [
        'Salary - Monthly', 'Freelance Project Payment', 'Dividend Income',
        'Interest Earned', 'Stock Sale Profit', 'Rental Income', 'Consulting Fee', 'Bonus',
    ],
    'Shopping': [
        'Amazon Purchase', 'Electronics - Laptop', 'Grocery Store', 'Clothing - Items',
        'Home Improvement', 'Books & Media', 'Pet Supplies', 'Health & Beauty',
    ],
    'Food & Dining': [
        'Restaurant - Dinner', 'Coffee Shop', 'Fast Food', 'Groceries - Whole Foods',
        'Groceries - Costco', 'Food Delivery', 'Takeout', 'Groceries - Trader Joes',
    ],
    'Transportation': [
        'Gas Station', 'Uber Ride', 'Lyft Ride', 'Car Insurance', 'Car Maintenance',
        'Parking Fee', 'Toll Road', 'Public Transit',
    ],
    'Entertainment': [
        'Netflix Subscription', 'Spotify Subscription', 'Movie Theater', 'Concert Tickets',
        'Gaming - Purchase', 'Sports Event', 'Hobby Supplies', 'Streaming Services',
    ],
    'Bills & Utilities': [
        'Electric Bill', 'Water Bill', 'Internet Service', 'Phone Bill', 'Insurance Premium',
        'Rent Payment', 'Mortgage Payment', 'Property Tax',
    ],
    'Healthcare': [
        'Doctor Visit', 'Pharmacy - Prescription', 'Dental Checkup', 'Vision Care',
        'Health Insurance', 'Medical Test', 'Therapy Session', 'Gym Membership',
    ],
    'Travel': [
        'Flight Booking', 'Hotel Stay', 'Airbnb Rental', 'Car Rental', 'Travel Insurance',
        'Restaurant - Travel', 'Souvenirs', 'Tour Booking',
    ],
}


class Command(BaseCommand):
    help = 'Generate synthetic finance data'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--count', '-n', type=int, default=500,
            help='Number of transactions to generate'
        )
        parser.add_argument(
            '--output', '-o', type=str, default='finance_data.csv',
            help='Output CSV file path'
        )
    
    def handle(self, *args, **options):
        n = options['count']
        output = options['output']
        
        self.stdout.write(f'Generating {n} transactions...')
        
        random.seed(42)
        data = []
        start_date = datetime.now() - timedelta(days=365)
        
        for i in range(n):
            days_offset = random.randint(0, 365)
            hours_offset = random.randint(0, 23)
            minutes_offset = random.randint(0, 59)
            timestamp = start_date + timedelta(
                days=days_offset, hours=hours_offset, minutes=minutes_offset
            )
            
            category = random.choice(list(CATEGORIES.keys()))
            description = random.choice(CATEGORIES[category])
            
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
            else:
                amount = random.uniform(5, 500)
            
            if category != 'Income':
                amount = -abs(amount)
            
            data.append({
                'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'description': description,
                'amount': round(amount, 2)
            })
        
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp').reset_index(drop=True)
        df.to_csv(output, index=False)
        
        total_income = df[df['amount'] > 0]['amount'].sum()
        total_expenses = abs(df[df['amount'] < 0]['amount'].sum())
        
        self.stdout.write(self.style.SUCCESS(
            f'Generated {len(df)} transactions → {output}'
        ))
        self.stdout.write(f'Income: ${total_income:,.2f}')
        self.stdout.write(f'Expenses: ${total_expenses:,.2f}')
        self.stdout.write(f'Net: ${total_income - total_expenses:,.2f}')
