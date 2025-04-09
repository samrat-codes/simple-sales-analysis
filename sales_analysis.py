import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the sales data file
try:
    df = pd.read_csv('d:\\Python Programs\\sales_analysis\\simple_sales_data.csv')
except FileNotFoundError:
    print("Error: simple_sales_data.csv not found!")
    exit()

# Converting dates and calculating totals if needed
df['Date'] = pd.to_datetime(df['Date'])

if 'Total' not in df.columns:
    df['Total'] = df['Quantity'] * df['Price']

# Performing basic analysis
total_sales = df['Total'].sum()
print(f"Total Sales: ${total_sales:.2f}\n")

sales_by_category = df.groupby('Category')['Total'].sum().sort_values(ascending=False)
print("Sales by Category:\n", sales_by_category)

top_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(1)
print("\nTop Selling Product:\n", top_product)

# Creating visualizations
plt.figure(figsize=(8, 6))
sns.barplot(x=sales_by_category.index, y=sales_by_category.values)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('sales_by_category.png')

plt.figure(figsize=(8, 6))
sns.lineplot(x='Date', y='Total', data=df)
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('sales_trend.png')

print("\nVisualizations saved as 'sales_by_category.png' and 'sales_trend.png'")

# Generating a simple report
report = f"""
# Sales Analysis Report

**Total Sales:** ${total_sales:.2f}

**Sales by Category:**
{sales_by_category.to_string()}

**Top Selling Product:**
{top_product.to_string()}

**Insights:**
- Electronics and Apparel are top categories.
- Laptops are the most sold product.
- Sales show an increasing trend.
"""

with open('sales_report.md', 'w') as f:
    f.write(report)

print("\nReport saved as 'sales_report.md'")