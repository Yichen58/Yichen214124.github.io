"""
Advanced Data Exploration - Module 4
=====================================

Now that you can read data, let's learn more advanced techniques for understanding
your dataset. This includes handling missing data, creating cross-tabulations,
and using pandas' powerful describe() method.

Learning Goals:
- Use describe() for comprehensive statistics
- Check for missing data and duplicates
- Create cross-tabulations (crosstabs)
- Calculate correlations between variables
- Create new calculated columns
- Handle categorical data effectively
"""

import pandas as pd
import numpy as np

print("=== LESSON 1: Comprehensive Data Overview ===")
print()

# Load our data
df = pd.read_csv('data/airbnb_sample.csv')

# The describe() method gives us a complete statistical summary
print("Complete statistical summary of numerical columns:")
print(df.describe())
print()

# For categorical columns, we can use include='object'
print("Summary of categorical columns:")
print(df.describe(include='object'))
print()

# Get information about data types and missing values
print("Data types and missing values:")
print(df.info())

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. CHECKING DATA QUALITY
# ============================================================================

print("=== LESSON 2: Data Quality Checks ===")
print()

# Check for missing values
print("Missing values in each column:")
missing_values = df.isnull().sum()
print(missing_values)
print()

# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
print()

# Check for unusual values in price column
print("Price distribution check:")
print(f"Minimum price: ${df['price'].min()}")
print(f"Maximum price: ${df['price'].max()}")
print(f"Properties with price = 0: {(df['price'] == 0).sum()}")
print(f"Properties with very high prices (>$1000): {(df['price'] > 1000).sum()}")
print()

# Check review scores (should be between 1-5)
print("Review score range check:")
print(f"Min review score: {df['review_score'].min()}")
print(f"Max review score: {df['review_score'].max()}")
print(f"Invalid review scores (<1 or >5): {((df['review_score'] < 1) | (df['review_score'] > 5)).sum()}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. CROSS-TABULATION ANALYSIS
# ============================================================================

print("=== LESSON 3: Cross-Tabulation Analysis ===")
print()

# Cross-tabulation shows relationships between categorical variables
print("Properties by Neighborhood and Property Type:")
crosstab = pd.crosstab(df['neighborhood'], df['property_type'])
print(crosstab)
print()

# Add margins (totals) to crosstab
print("Same table with totals:")
crosstab_with_totals = pd.crosstab(df['neighborhood'], df['property_type'], margins=True)
print(crosstab_with_totals)
print()

# Cross-tabulation with averages
print("Average price by Neighborhood and Property Type:")
price_crosstab = pd.crosstab(df['neighborhood'], df['property_type'], 
                           values=df['price'], aggfunc='mean')
print(price_crosstab.round(2))

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. CORRELATION ANALYSIS
# ============================================================================

print("=== LESSON 4: Understanding Relationships Between Variables ===")
print()

# Select only numerical columns for correlation
numerical_columns = ['price', 'bedrooms', 'bathrooms', 'accommodates', 
                    'review_score', 'availability_365', 'host_response_rate']

# Calculate correlation matrix
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix (values closer to 1 or -1 indicate stronger relationships):")
print(correlation_matrix.round(3))
print()

# Find strong correlations with price
print("Variables most correlated with price:")
price_correlations = correlation_matrix['price'].abs().sort_values(ascending=False)
for variable, correlation in price_correlations.items():
    if variable != 'price':  # Don't show price with itself
        print(f"{variable}: {correlation:.3f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. CREATING NEW CALCULATED COLUMNS
# ============================================================================

print("=== LESSON 5: Creating Business Metrics ===")
print()

# Create new columns for business analysis
df_analysis = df.copy()  # Make a copy so we don't modify the original

# Calculate price per bedroom
df_analysis['price_per_bedroom'] = df_analysis['price'] / df_analysis['bedrooms']

# Calculate annual revenue potential (assuming full booking)
df_analysis['annual_revenue_potential'] = df_analysis['price'] * df_analysis['availability_365']

# Create price categories
def categorize_price(price):
    if price < 100:
        return 'Budget'
    elif price < 200:
        return 'Mid-range'
    else:
        return 'Luxury'

df_analysis['price_category'] = df_analysis['price'].apply(categorize_price)

# Create high-rated flag (4.5 and above)
df_analysis['high_rated'] = df_analysis['review_score'] >= 4.5

print("New calculated columns:")
print(df_analysis[['listing_id', 'price', 'bedrooms', 'price_per_bedroom', 
                  'annual_revenue_potential', 'price_category', 'high_rated']].head())

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. ADVANCED GROUPING AND AGGREGATION
# ============================================================================

print("=== LESSON 6: Advanced Business Analysis ===")
print()

# Multiple aggregations at once
price_analysis = df_analysis.groupby('neighborhood')['price'].agg([
    'count',    # number of properties
    'mean',     # average price
    'median',   # median price
    'std',      # standard deviation
    'min',      # minimum price
    'max'       # maximum price
]).round(2)

print("Comprehensive price analysis by neighborhood:")
print(price_analysis)
print()

# Analysis by price category
category_analysis = df_analysis.groupby('price_category').agg({
    'price': ['count', 'mean'],
    'review_score': 'mean',
    'availability_365': 'mean',
    'accommodates': 'mean'
}).round(2)

print("Analysis by price category:")
print(category_analysis)
print()

# Performance analysis: high-rated vs others
performance_comparison = df_analysis.groupby('high_rated').agg({
    'price': 'mean',
    'availability_365': 'mean',
    'host_response_rate': 'mean',
    'accommodates': 'mean'
}).round(2)

print("High-rated vs lower-rated property comparison:")
print(performance_comparison)

print("\n" + "="*50 + "\n")

# ============================================================================
# 7. ADVANCED FILTERING
# ============================================================================

print("=== LESSON 7: Complex Business Queries ===")
print()

# Complex multi-condition filtering
premium_properties = df_analysis[
    (df_analysis['price'] > 150) &          # Expensive
    (df_analysis['review_score'] >= 4.5) &  # High-rated
    (df_analysis['bedrooms'] >= 2) &        # At least 2 bedrooms
    (df_analysis['instant_bookable'] == True)  # Instant bookable
]

print(f"Premium properties (expensive, high-rated, 2+ bedrooms, instant bookable): {len(premium_properties)}")
if len(premium_properties) > 0:
    print("These properties:")
    print(premium_properties[['listing_id', 'neighborhood', 'property_type', 
                            'price', 'bedrooms', 'review_score']])
print()

# Find underpriced high-quality properties
underpriced = df_analysis[
    (df_analysis['review_score'] >= 4.5) &  # High quality
    (df_analysis['price'] < df_analysis['price'].median())  # Below median price
]

print(f"Underpriced high-quality properties: {len(underpriced)}")
if len(underpriced) > 0:
    print("These might be good deals:")
    print(underpriced[['listing_id', 'neighborhood', 'price', 'review_score']].sort_values('price'))

print("\n" + "="*50 + "\n")

# ============================================================================
# 8. BUSINESS INSIGHTS SUMMARY
# ============================================================================

print("=== LESSON 8: Key Business Insights ===")
print()

# Top insights from our analysis
print("KEY FINDINGS:")
print("-" * 40)

# 1. Best performing neighborhood
best_neighborhood = df_analysis.groupby('neighborhood')['price'].mean().idxmax()
best_avg_price = df_analysis.groupby('neighborhood')['price'].mean().max()
print(f"1. Most profitable neighborhood: {best_neighborhood} (${best_avg_price:.2f} avg)")

# 2. Property type with best reviews
best_property_type = df_analysis.groupby('property_type')['review_score'].mean().idxmax()
best_review_score = df_analysis.groupby('property_type')['review_score'].mean().max()
print(f"2. Highest-rated property type: {best_property_type} ({best_review_score:.2f} avg)")

# 3. Sweet spot for pricing
median_price = df_analysis['price'].median()
high_rated_count = len(df_analysis[df_analysis['review_score'] >= 4.5])
total_count = len(df_analysis)
print(f"3. Median price point: ${median_price:.2f}")
print(f"4. {high_rated_count}/{total_count} properties ({high_rated_count/total_count*100:.1f}%) are high-rated (4.5+)")

# 5. Availability insights
avg_availability = df_analysis['availability_365'].mean()
print(f"5. Average availability: {avg_availability:.0f} days per year")

print("\n" + "="*50)
print("Excellent! You now know how to thoroughly explore datasets!")
print("Next: Run 05_data_cleaning.py to learn about cleaning data")
print("="*50)