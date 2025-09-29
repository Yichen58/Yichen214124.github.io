"""
Data Visualization for Business - Module 7
===========================================

"A picture is worth a thousand words" - especially in business! Learn to create
clear, professional charts that tell your data story effectively.

Learning Goals:
- Create bar charts for categorical data
- Make histograms for numerical distributions
- Build scatter plots to show relationships
- Design box plots for group comparisons
- Choose the right chart type for your message
- Format charts professionally
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set up matplotlib for better-looking charts
plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

print("=== LESSON 1: Your First Business Chart ===")
print()

# Load data
try:
    df = pd.read_csv('data/airbnb_cleaned.csv')
    print("✅ Using cleaned dataset")
except FileNotFoundError:
    df = pd.read_csv('data/airbnb_sample.csv')
    print("✅ Using original dataset")

print(f"Creating visualizations for {len(df)} properties")
print()

# Create our first chart: Properties by neighborhood
neighborhood_counts = df['neighborhood'].value_counts()

plt.figure(figsize=(10, 6))
bars = plt.bar(neighborhood_counts.index, neighborhood_counts.values, color='skyblue', alpha=0.8)
plt.title('Number of Properties by Neighborhood', fontsize=14, fontweight='bold')
plt.xlabel('Neighborhood', fontsize=12)
plt.ylabel('Number of Properties', fontsize=12)
plt.xticks(rotation=45)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

print("💡 Business Insight: This chart shows market concentration by area")
print("   Use this to identify where to focus marketing or find opportunities")

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. PRICE DISTRIBUTION HISTOGRAM
# ============================================================================

print("=== LESSON 2: Understanding Price Distribution ===")
print()

plt.figure(figsize=(12, 5))

# Create a histogram with professional styling
plt.subplot(1, 2, 1)
plt.hist(df['price'], bins=15, color='lightcoral', alpha=0.7, edgecolor='black')
plt.title('Price Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Price ($)', fontsize=12)
plt.ylabel('Number of Properties', fontsize=12)
plt.grid(True, alpha=0.3)

# Add mean and median lines
mean_price = df['price'].mean()
median_price = df['price'].median()
plt.axvline(mean_price, color='red', linestyle='--', label=f'Mean: ${mean_price:.0f}')
plt.axvline(median_price, color='blue', linestyle='-', label=f'Median: ${median_price:.0f}')
plt.legend()

# Create a box plot to show quartiles
plt.subplot(1, 2, 2)
box_plot = plt.boxplot(df['price'], patch_artist=True)
box_plot['boxes'][0].set_facecolor('lightgreen')
box_plot['boxes'][0].set_alpha(0.7)
plt.title('Price Distribution (Box Plot)', fontsize=14, fontweight='bold')
plt.ylabel('Price ($)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("💡 Business Insight: Histograms show the shape of your market")
print("   Box plots highlight outliers and quartiles for pricing strategy")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. COMPARING GROUPS WITH BAR CHARTS
# ============================================================================

print("=== LESSON 3: Comparing Property Types ===")
print()

# Average price by property type
avg_price_by_type = df.groupby('property_type')['price'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(avg_price_by_type.index, avg_price_by_type.values, 
               color=['gold', 'lightblue', 'lightgreen', 'coral'])
plt.title('Average Price by Property Type', fontsize=14, fontweight='bold')
plt.xlabel('Property Type', fontsize=12)
plt.ylabel('Average Price ($)', fontsize=12)
plt.xticks(rotation=45)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 3,
             f'${height:.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

print("💡 Business Insight: Compare performance across categories")
print("   Identify which property types command premium prices")

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. SCATTER PLOTS FOR RELATIONSHIPS
# ============================================================================

print("=== LESSON 4: Exploring Price Relationships ===")
print()

plt.figure(figsize=(12, 5))

# Price vs Bedrooms
plt.subplot(1, 2, 1)
plt.scatter(df['bedrooms'], df['price'], alpha=0.6, color='purple')
plt.title('Price vs Number of Bedrooms', fontsize=12, fontweight='bold')
plt.xlabel('Number of Bedrooms', fontsize=11)
plt.ylabel('Price ($)', fontsize=11)
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['bedrooms'], df['price'], 1)
p = np.poly1d(z)
plt.plot(df['bedrooms'], p(df['bedrooms']), "r--", alpha=0.8, label='Trend line')
plt.legend()

# Price vs Review Score
plt.subplot(1, 2, 2)
plt.scatter(df['review_score'], df['price'], alpha=0.6, color='green')
plt.title('Price vs Review Score', fontsize=12, fontweight='bold')
plt.xlabel('Review Score', fontsize=11)
plt.ylabel('Price ($)', fontsize=11) 
plt.grid(True, alpha=0.3)

# Add trend line
z2 = np.polyfit(df['review_score'], df['price'], 1)
p2 = np.poly1d(z2)
plt.plot(df['review_score'], p2(df['review_score']), "r--", alpha=0.8, label='Trend line')
plt.legend()

plt.tight_layout()
plt.show()

print("💡 Business Insight: Scatter plots reveal correlations")
print("   Use these to understand what drives pricing in your market")

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. MULTI-GROUP COMPARISONS
# ============================================================================

print("=== LESSON 5: Advanced Group Comparisons ===")
print()

# Create grouped bar chart: Average price by neighborhood and property type
pivot_data = df.pivot_table(values='price', index='neighborhood', 
                           columns='property_type', aggfunc='mean', fill_value=0)

plt.figure(figsize=(12, 6))
pivot_data.plot(kind='bar', ax=plt.gca(), width=0.8)
plt.title('Average Price by Neighborhood and Property Type', fontsize=14, fontweight='bold')
plt.xlabel('Neighborhood', fontsize=12)
plt.ylabel('Average Price ($)', fontsize=12)
plt.legend(title='Property Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("💡 Business Insight: Grouped charts show complex relationships")
print("   Identify which combinations of features are most valuable")

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. PIE CHARTS FOR COMPOSITION
# ============================================================================

print("=== LESSON 6: Market Composition Analysis ===")
print()

plt.figure(figsize=(12, 5))

# Property type distribution
plt.subplot(1, 2, 1)
property_counts = df['property_type'].value_counts()
colors = ['gold', 'lightblue', 'lightgreen', 'coral']
plt.pie(property_counts.values, labels=property_counts.index, autopct='%1.1f%%',
        colors=colors, startangle=90)
plt.title('Market Share by Property Type', fontsize=12, fontweight='bold')

# Price category distribution
plt.subplot(1, 2, 2)
price_categories = pd.cut(df['price'], bins=[0, 100, 200, float('inf')], 
                         labels=['Budget (<$100)', 'Mid-range ($100-199)', 'Luxury ($200+)'])
category_counts = price_categories.value_counts()
colors2 = ['lightcoral', 'gold', 'lightgreen']
plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%',
        colors=colors2, startangle=90)
plt.title('Market Share by Price Category', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

print("💡 Business Insight: Pie charts show market composition")
print("   Understand your competitive landscape and market segments")

print("\n" + "="*50 + "\n")

# ============================================================================
# 7. TIME SERIES STYLE ANALYSIS
# ============================================================================

print("=== LESSON 7: Performance Metrics Dashboard ===")
print()

# Create a dashboard-style visualization
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Chart 1: Price by neighborhood (horizontal bar)
neighborhood_avg = df.groupby('neighborhood')['price'].mean().sort_values()
ax1.barh(neighborhood_avg.index, neighborhood_avg.values, color='skyblue')
ax1.set_title('Average Price by Neighborhood', fontweight='bold')
ax1.set_xlabel('Price ($)')

# Chart 2: Review score distribution
ax2.hist(df['review_score'], bins=10, color='lightgreen', alpha=0.7, edgecolor='black')
ax2.set_title('Review Score Distribution', fontweight='bold')
ax2.set_xlabel('Review Score')
ax2.set_ylabel('Count')

# Chart 3: Bedrooms vs Price (box plot)
bedroom_data = [df[df['bedrooms'] == i]['price'].values for i in df['bedrooms'].unique()]
ax3.boxplot(bedroom_data, labels=sorted(df['bedrooms'].unique()))
ax3.set_title('Price Distribution by Bedrooms', fontweight='bold')
ax3.set_xlabel('Number of Bedrooms')
ax3.set_ylabel('Price ($)')

# Chart 4: Accommodates vs Price
ax4.scatter(df['accommodates'], df['price'], alpha=0.6, color='orange')
ax4.set_title('Price vs Guest Capacity', fontweight='bold')
ax4.set_xlabel('Maximum Guests')
ax4.set_ylabel('Price ($)')

plt.tight_layout()
plt.show()

print("💡 Business Insight: Dashboards tell a complete story")
print("   Multiple related charts provide comprehensive market view")

print("\n" + "="*50 + "\n")

# ============================================================================
# 8. CUSTOMIZING CHARTS FOR PRESENTATIONS
# ============================================================================

print("=== LESSON 8: Professional Chart Formatting ===")
print()

# Create a publication-ready chart
plt.figure(figsize=(12, 7))

# Data for the chart
monthly_performance = {
    'Jan': 145, 'Feb': 158, 'Mar': 172, 'Apr': 189, 'May': 201, 'Jun': 218,
    'Jul': 234, 'Aug': 229, 'Sep': 198, 'Oct': 176, 'Nov': 162, 'Dec': 149
}

months = list(monthly_performance.keys())
prices = list(monthly_performance.values())

# Create professional line chart
plt.plot(months, prices, marker='o', linewidth=3, markersize=8, color='#2E86AB')
plt.fill_between(months, prices, alpha=0.3, color='#2E86AB')

# Professional formatting
plt.title('Seasonal Price Trends - Airbnb Market Analysis', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Nightly Rate ($)', fontsize=14)
plt.grid(True, alpha=0.3)

# Add annotations for key insights
max_month = max(monthly_performance, key=monthly_performance.get)
max_price = monthly_performance[max_month]
plt.annotate(f'Peak Season\n${max_price}', 
             xy=(max_month, max_price), xytext=(max_month, max_price + 20),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, ha='center', fontweight='bold')

plt.ylim(130, 250)
plt.tight_layout()
plt.show()

print("💡 Business Insight: Professional formatting enhances credibility")
print("   Clean, annotated charts communicate insights effectively")

print("\n" + "="*50 + "\n")

# ============================================================================
# 9. CHART SELECTION GUIDE
# ============================================================================

print("=== LESSON 9: Choosing the Right Chart Type ===")
print()

chart_guide = {
    'Bar Chart': 'Comparing categories (e.g., price by neighborhood)',
    'Histogram': 'Distribution of numerical data (e.g., price distribution)',
    'Scatter Plot': 'Relationship between two numbers (e.g., bedrooms vs price)',
    'Line Chart': 'Trends over time (e.g., seasonal pricing)',
    'Pie Chart': 'Parts of a whole (e.g., market share by property type)',
    'Box Plot': 'Comparing distributions between groups',
    'Heatmap': 'Correlation matrix or two-dimensional patterns'
}

print("CHART SELECTION GUIDE:")
print("=" * 30)
for chart_type, use_case in chart_guide.items():
    print(f"{chart_type:<12}: {use_case}")

print()
print("BEST PRACTICES:")
print("-" * 20)
print("✅ Keep it simple - one main message per chart")
print("✅ Use clear titles and labels")
print("✅ Choose colors that are colorblind-friendly")
print("✅ Add data labels when helpful")
print("✅ Remove chart junk (unnecessary elements)")
print("✅ Consider your audience (technical vs. executive)")
print("✅ Always include units (e.g., $, %, days)")

print("\n" + "="*50 + "\n")

# ============================================================================
# 10. BUSINESS DASHBOARD SUMMARY
# ============================================================================

print("=== LESSON 10: Your Data Visualization Toolkit ===")
print()

print("CONGRATULATIONS! You now know how to:")
print("=" * 45)
print("📊 Create bar charts for categorical comparisons")
print("📈 Build histograms to show data distributions") 
print("🔍 Use scatter plots to explore relationships")
print("📦 Make box plots for group comparisons")
print("🥧 Design pie charts for composition analysis")
print("📋 Build multi-chart dashboards")
print("✨ Format charts professionally")
print("🎯 Choose the right chart for your message")
print()

print("NEXT STEPS:")
print("-" * 15)
print("• Practice with your own data")
print("• Experiment with colors and styles")
print("• Create charts that tell a story")
print("• Share insights with stakeholders")
print("• Build interactive dashboards")

print("\n" + "="*50)
print("Amazing work! You're now a data visualization pro!")
print("Next: Run 08_business_insights.py to tie everything together")
print("="*50)