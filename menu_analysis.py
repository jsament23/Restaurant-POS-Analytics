import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the bulk data
df_raw = pd.read_csv('restaurant_transactions.csv')

# Aggregate the data
menu_stats = df_raw.groupby('item_name').agg(
    units_sold=('item_name', 'count'),
    avg_price=('menu_price', 'mean'),
    avg_cost=('food_cost', 'mean')
).reset_index()

menu_stats['margin'] = menu_stats['avg_price'] - menu_stats['avg_cost']

# Quadrant Logic
avg_margin = menu_stats['margin'].mean()
avg_vol = menu_stats['units_sold'].mean()

# Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(data=menu_stats, x='units_sold', y='margin', s=100, color='darkblue')

# Add Quadrant Lines
plt.axvline(avg_vol, color='red', linestyle='--', alpha=0.5)
plt.axhline(avg_margin, color='red', linestyle='--', alpha=0.5)

# Annotate points
for i in range(menu_stats.shape[0]):
    plt.text(menu_stats.units_sold[i]+2, menu_stats.margin[i], menu_stats.item_name[i])

plt.title('Menu Engineering Matrix (Toast Analytics Style)')
plt.xlabel('Popularity (Units Sold)')
plt.ylabel('Profitability (Margin $)')
plt.savefig('menu_matrix_chart.png')
print("✅ Visualization saved as 'menu_matrix_chart.png'")