import pandas as pd
import numpy as np
pip install seaborn matplotlib

# 1. POS
data = {
    'item_name': ['Truffle Fries', 'Classic Burger', 'Ribeye Steak', 'House Salad', 'Lobster Roll', 'Soda'],
    'category': ['App', 'Main', 'Main', 'App', 'Main', 'Beverage'],
    'units_sold': [450, 600, 150, 300, 80, 800],
    'menu_price': [12, 18, 45, 10, 35, 3.5],
    'food_cost': [3, 6, 22, 2, 25, 0.5]
}

df = pd.DataFrame(data)

# 2. Calculations
df['contribution_margin'] = df['menu_price'] - df['food_cost']
df['total_profit'] = df['units_sold'] * df['contribution_margin']

# 3. Categorization Logic
avg_margin = df['contribution_margin'].mean()
avg_popularity = df['units_sold'].mean()

def categorize(row):
    if row['contribution_margin'] >= avg_margin and row['units_sold'] >= avg_popularity:
        return 'Star (High Profit, High Popularity)'
    if row['contribution_margin'] < avg_margin and row['units_sold'] >= avg_popularity:
        return 'Plowhorse (Low Profit, High Popularity)'
    if row['contribution_margin'] >= avg_margin and row['units_sold'] < avg_popularity:
        return 'Puzzle (High Profit, Low Popularity)'
    return 'Dog (Low Profit, Low Popularity)'

df['menu_designation'] = df.apply(categorize, axis=1)

print(df[['item_name', 'menu_designation']])
