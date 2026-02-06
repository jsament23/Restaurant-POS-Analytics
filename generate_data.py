import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Configuration
items = ['Classic Burger', 'Truffle Fries', 'Ribeye Steak', 'House Salad', 'Lobster Roll', 'Soda', 'Draft Beer', 'Cheesecake']
categories = ['Main', 'App', 'Main', 'App', 'Main', 'Beverage', 'Beverage', 'Dessert']
prices = [15.00, 9.00, 42.00, 12.00, 32.00, 3.50, 7.00, 10.00]
costs = [5.00, 2.50, 18.00, 3.00, 22.00, 0.50, 1.50, 4.00]

# Generate 1,000 rows of transactions
n_rows = 1000
data = {
    'transaction_id': range(1, n_rows + 1),
    'item_name': np.random.choice(items, n_rows),
    'timestamp': pd.to_datetime('2026-01-01') + pd.to_timedelta(np.random.randint(0, 30, n_rows), unit='D')
}

df = pd.DataFrame(data)

# Map prices and costs
item_map = pd.DataFrame({'item_name': items, 'menu_price': prices, 'food_cost': costs, 'category': categories})
df = df.merge(item_map, on='item_name')

df.to_csv('restaurant_transactions.csv', index=False)
print("✅ Created 'restaurant_transactions.csv' with 1,000 rows.")