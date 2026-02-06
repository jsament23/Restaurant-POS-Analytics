import pandas as pd

# 1. Setup the data (Simulating a Restaurant POS Export)
data = {
    'item_name': ['Truffle Fries', 'Classic Burger', 'Ribeye Steak', 'House Salad', 'Lobster Roll', 'Soda'],
    'units_sold': [450, 600, 150, 300, 80, 800],
    'menu_price': [12.00, 18.00, 45.00, 10.00, 35.00, 3.50],
    'food_cost': [3.00, 6.00, 22.00, 2.00, 25.00, 0.50]
}

df = pd.DataFrame(data)

# 2. Calculate Key Performance Indicators (KPIs)
df['margin'] = df['menu_price'] - df['food_cost']
df['total_profit'] = df['units_sold'] * df['margin']

# 3. Define the Menu Matrix Logic
avg_margin = df['margin'].mean()
avg_vol = df['units_sold'].mean()

def get_category(row):
    if row['margin'] >= avg_margin and row['units_sold'] >= avg_vol:
        return 'Star'
    if row['margin'] < avg_margin and row['units_sold'] >= avg_vol:
        return 'Plowhorse'
    if row['margin'] >= avg_margin and row['units_sold'] < avg_vol:
        return 'Puzzle'
    return 'Dog'

df['category'] = df.apply(get_category, axis=1)

# 4. Save and Print Results
print("--- Menu Engineering Analysis ---")
print(df[['item_name', 'units_sold', 'margin', 'category']])
df.to_csv('menu_analysis_results.csv', index=False)
print("\n✅ Success! 'menu_analysis_results.csv' has been created.")