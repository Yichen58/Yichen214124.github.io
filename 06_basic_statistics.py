"""
Basic Statistics for Business Analysis - Module 6
==================================================

Statistics are the foundation of data-driven business decisions. In this module,
you'll learn the essential statistical concepts every business analyst needs.

Learning Goals:
- Calculate measures of central tendency (mean, median, mode)
- Understand measures of variability (range, standard deviation)
- Use percentiles and quartiles
- Calculate business-relevant ratios and rates
- Compare groups statistically
- Interpret statistical results for business decisions
"""

import pandas as pd
import numpy as np

print("=== LESSON 1: Measures of Central Tendency ===")
print()

# Load our cleaned data (or original if cleaned doesn't exist)
try:
    df = pd.read_csv('data/airbnb_cleaned.csv')
    print("✅ Using cleaned dataset")
except FileNotFoundError:
    df = pd.read_csv('data/airbnb_sample.csv')
    print("✅ Using original dataset")

print(f"Dataset: {len(df)} properties")
print()

# Central Tendency: Where is the "center" of our data?
prices = df['price']

# Mean (average) - sum of all values divided by count
mean_price = prices.mean()
print(f"Mean (Average) Price: ${mean_price:.2f}")
print("  → This is what you get if you add all prices and divide by the number of properties")

# Median - the middle value when data is sorted
median_price = prices.median()
print(f"Median Price: ${median_price:.2f}")
print("  → Half of properties cost more than this, half cost less")

# Mode - the most frequently occurring value
mode_price = prices.mode()
if len(mode_price) > 0:
    print(f"Mode Price: ${mode_price[0]:.2f}")
    print("  → This price appears most frequently in our dataset")
else:
    print("Mode Price: No mode (all prices are unique)")

print()
print("💡 Business Interpretation:")
if mean_price > median_price:
    print("  Mean > Median suggests some very expensive properties are pulling the average up")
else:
    print("  Mean ≤ Median suggests prices are fairly evenly distributed")

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. MEASURES OF VARIABILITY
# ============================================================================

print("=== LESSON 2: Understanding Price Variability ===")
print()

# Range - difference between highest and lowest values
price_range = prices.max() - prices.min()
print(f"Price Range: ${price_range:.2f}")
print(f"  → Prices vary from ${prices.min():.2f} to ${prices.max():.2f}")

# Standard Deviation - how spread out the data is from the mean  
std_price = prices.std()
print(f"Standard Deviation: ${std_price:.2f}")
print("  → Most properties are priced within one standard deviation of the mean")
print(f"  → That's roughly ${mean_price - std_price:.2f} to ${mean_price + std_price:.2f}")

# Variance - square of standard deviation
variance_price = prices.var()
print(f"Variance: ${variance_price:.2f}")
print("  → This measures variability, but standard deviation is more interpretable")

print()
print("💡 Business Interpretation:")
coefficient_of_variation = (std_price / mean_price) * 100
print(f"  Coefficient of Variation: {coefficient_of_variation:.1f}%")
if coefficient_of_variation > 30:
    print("  → High variability - prices are quite diverse")
elif coefficient_of_variation > 15:
    print("  → Moderate variability - some price diversity")
else:
    print("  → Low variability - prices are fairly consistent")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. PERCENTILES AND QUARTILES
# ============================================================================

print("=== LESSON 3: Percentiles and Quartiles ===")
print()

# Quartiles divide data into four equal parts
q1 = prices.quantile(0.25)  # 25th percentile
q2 = prices.quantile(0.50)  # 50th percentile (median)
q3 = prices.quantile(0.75)  # 75th percentile

print("Price Quartiles:")
print(f"Q1 (25th percentile): ${q1:.2f}")
print(f"Q2 (50th percentile/Median): ${q2:.2f}")
print(f"Q3 (75th percentile): ${q3:.2f}")
print()

# Interquartile Range (IQR) - the middle 50% of data
iqr = q3 - q1
print(f"Interquartile Range (IQR): ${iqr:.2f}")
print("  → The middle 50% of properties fall within this price range")
print()

# Common business percentiles
percentiles = [10, 25, 50, 75, 90, 95, 99]
print("Key Business Percentiles:")
for p in percentiles:
    value = prices.quantile(p/100)
    print(f"{p}th percentile: ${value:.2f}")

print()
print("💡 Business Applications:")
print("  → 10th percentile: Budget-friendly options")
print("  → 50th percentile: Market median")
print("  → 90th percentile: Premium market")
print("  → 99th percentile: Luxury segment")

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. STATISTICS BY GROUPS
# ============================================================================

print("=== LESSON 4: Comparative Statistics by Groups ===")
print()

# Compare statistics across neighborhoods
print("Price Statistics by Neighborhood:")
neighborhood_stats = df.groupby('neighborhood')['price'].agg([
    'count',
    'mean', 
    'median',
    'std',
    'min',
    'max'
]).round(2)

print(neighborhood_stats)
print()

# Which neighborhood has the most consistent pricing?
print("Price Consistency Analysis:")
for neighborhood in df['neighborhood'].unique():
    neighborhood_prices = df[df['neighborhood'] == neighborhood]['price']
    cv = (neighborhood_prices.std() / neighborhood_prices.mean()) * 100
    print(f"{neighborhood}: {cv:.1f}% variation")

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. BUSINESS RATIOS AND RATES
# ============================================================================

print("=== LESSON 5: Business Performance Metrics ===")
print()

# Calculate important business ratios
print("Key Business Metrics:")
print("-" * 25)

# Average price per bedroom
df['price_per_bedroom'] = df['price'] / df['bedrooms']
avg_price_per_bedroom = df['price_per_bedroom'].mean()
print(f"Average price per bedroom: ${avg_price_per_bedroom:.2f}")

# Average price per person (accommodates)
df['price_per_person'] = df['price'] / df['accommodates']
avg_price_per_person = df['price_per_person'].mean()
print(f"Average price per person: ${avg_price_per_person:.2f}")

# Occupancy and revenue potential
avg_availability = df['availability_365'].mean()
avg_occupancy_rate = (365 - avg_availability) / 365
print(f"Average availability: {avg_availability:.0f} days")
print(f"Implied occupancy rate: {avg_occupancy_rate:.1%}")

# Revenue metrics
df['potential_annual_revenue'] = df['price'] * (365 - df['availability_365'])
avg_annual_revenue = df['potential_annual_revenue'].mean()
print(f"Average potential annual revenue: ${avg_annual_revenue:.0f}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. QUALITY METRICS
# ============================================================================

print("=== LESSON 6: Quality and Performance Statistics ===")
print()

# Review score analysis
review_stats = df['review_score'].describe()
print("Review Score Statistics:")
print(review_stats.round(2))
print()

# Quality categories
def quality_category(score):
    if score >= 4.7:
        return 'Excellent'
    elif score >= 4.3:
        return 'Very Good'
    elif score >= 4.0:
        return 'Good'
    else:
        return 'Needs Improvement'

df['quality_category'] = df['review_score'].apply(quality_category)
quality_distribution = df['quality_category'].value_counts()

print("Quality Distribution:")
for category, count in quality_distribution.items():
    percentage = (count / len(df)) * 100
    print(f"{category}: {count} properties ({percentage:.1f}%)")

print("\n" + "="*50 + "\n")

# ============================================================================
# 7. CORRELATION ANALYSIS
# ============================================================================

print("=== LESSON 7: Understanding Relationships ===")
print()

# Calculate correlations between key variables
correlation_vars = ['price', 'bedrooms', 'bathrooms', 'accommodates', 'review_score']
correlations = df[correlation_vars].corr()['price'].sort_values(ascending=False)

print("Variables correlated with price:")
for variable, correlation in correlations.items():
    if variable != 'price':
        strength = "Strong" if abs(correlation) > 0.7 else "Moderate" if abs(correlation) > 0.3 else "Weak"
        direction = "positive" if correlation > 0 else "negative"
        print(f"{variable}: {correlation:.3f} ({strength} {direction})")

print()

# Business interpretation of correlations
print("💡 Business Insights from Correlations:")
accommodates_corr = correlations['accommodates']
bedrooms_corr = correlations['bedrooms']
if accommodates_corr > 0.5:
    print("  → Larger properties (more guests) command higher prices")
if bedrooms_corr > 0.5:
    print("  → More bedrooms strongly correlate with higher prices")

print("\n" + "="*50 + "\n")

# ============================================================================
# 8. STATISTICAL COMPARISON OF GROUPS
# ============================================================================

print("=== LESSON 8: Comparing Different Property Types ===")
print()

# Compare property types statistically
property_comparison = df.groupby('property_type').agg({
    'price': ['count', 'mean', 'median', 'std'],
    'review_score': 'mean',
    'accommodates': 'mean'
}).round(2)

print("Property Type Comparison:")
print(property_comparison)
print()

# Find the best value proposition
print("Value Analysis (Price per Person by Property Type):")
value_analysis = df.groupby('property_type')['price_per_person'].agg(['mean', 'median']).round(2)
print(value_analysis)
print()

# Statistical significance test (simplified explanation)
apartment_prices = df[df['property_type'] == 'Apartment']['price']
house_prices = df[df['property_type'] == 'House']['price']

if len(apartment_prices) > 0 and len(house_prices) > 0:
    apt_mean = apartment_prices.mean()
    house_mean = house_prices.mean()
    difference = abs(apt_mean - house_mean)
    
    print(f"Price difference between Apartments and Houses:")
    print(f"  Apartment average: ${apt_mean:.2f}")
    print(f"  House average: ${house_mean:.2f}")
    print(f"  Difference: ${difference:.2f}")
    
    if difference > 50:
        print("  → Substantial price difference between property types")
    else:
        print("  → Similar pricing between property types")

print("\n" + "="*50 + "\n")

# ============================================================================
# 9. EXECUTIVE SUMMARY
# ============================================================================

print("=== LESSON 9: Executive Summary of Key Statistics ===")
print()

print("AIRBNB MARKET ANALYSIS - KEY FINDINGS")
print("=" * 45)
print()

print("PRICING OVERVIEW:")
print(f"  • Average nightly rate: ${mean_price:.2f}")
print(f"  • Median nightly rate: ${median_price:.2f}")
print(f"  • Price range: ${prices.min():.2f} - ${prices.max():.2f}")
print(f"  • Standard deviation: ${std_price:.2f}")
print()

print("MARKET SEGMENTS:")
budget_count = len(df[df['price'] < 100])
mid_count = len(df[(df['price'] >= 100) & (df['price'] < 200)])
luxury_count = len(df[df['price'] >= 200])

print(f"  • Budget (<$100): {budget_count} properties ({budget_count/len(df)*100:.1f}%)")
print(f"  • Mid-range ($100-199): {mid_count} properties ({mid_count/len(df)*100:.1f}%)")
print(f"  • Luxury ($200+): {luxury_count} properties ({luxury_count/len(df)*100:.1f}%)")
print()

print("QUALITY METRICS:")
print(f"  • Average review score: {df['review_score'].mean():.2f}/5.0")
high_rated = len(df[df['review_score'] >= 4.5])
print(f"  • High-rated properties (4.5+): {high_rated} ({high_rated/len(df)*100:.1f}%)")
print()

print("BUSINESS OPPORTUNITIES:")
best_value_neighborhood = df.groupby('neighborhood')['price_per_person'].mean().idxmin()
print(f"  • Best value neighborhood: {best_value_neighborhood}")
most_expensive_neighborhood = df.groupby('neighborhood')['price'].mean().idxmax()
print(f"  • Premium market: {most_expensive_neighborhood}")

print("\n" + "="*50)
print("Congratulations! You now understand business statistics!")
print("Next: Run 07_simple_charts.py to visualize your data")
print("="*50)