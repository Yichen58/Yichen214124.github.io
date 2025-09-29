"""
Business Insights from Data Analysis - Module 8
================================================

This is where data analysis becomes business intelligence! Learn to translate
your analytical findings into actionable business recommendations.

Learning Goals:
- Synthesize findings from multiple analyses
- Identify business opportunities and risks
- Create executive summaries
- Make data-driven recommendations
- Present insights in business language
- Calculate ROI and business impact
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=== EXECUTIVE SUMMARY: AIRBNB MARKET ANALYSIS ===")
print()

# Load data
try:
    df = pd.read_csv('data/airbnb_cleaned.csv')
    print("✅ Analysis based on cleaned dataset")
except FileNotFoundError:
    df = pd.read_csv('data/airbnb_sample.csv')
    print("✅ Analysis based on original dataset")

print(f"📊 Dataset: {len(df)} properties analyzed")
print(f"📅 Analysis Date: {pd.Timestamp.now().strftime('%B %Y')}")
print()

print("="*60)
print(" BUSINESS INTELLIGENCE REPORT")
print("="*60)

print("\n" + "="*50 + "\n")

# ============================================================================
# 1. MARKET OVERVIEW AND SIZE
# ============================================================================

print("=== 1. MARKET OVERVIEW ===")
print()

# Calculate market metrics
total_properties = len(df)
avg_price = df['price'].mean()
median_price = df['price'].median()
total_potential_revenue = (df['price'] * (365 - df['availability_365'])).sum()
avg_property_revenue = total_potential_revenue / total_properties

print("MARKET METRICS:")
print("-" * 20)
print(f"🏠 Total Properties Analyzed: {total_properties:,}")
print(f"💰 Average Nightly Rate: ${avg_price:.2f}")
print(f"📈 Median Nightly Rate: ${median_price:.2f}")
print(f"📊 Price Range: ${df['price'].min():.2f} - ${df['price'].max():.2f}")
print(f"💸 Total Market Revenue Potential: ${total_potential_revenue:,.0f}")
print(f"📋 Average Property Annual Revenue: ${avg_property_revenue:,.0f}")

# Market segments
budget_properties = len(df[df['price'] < 100])
midrange_properties = len(df[(df['price'] >= 100) & (df['price'] < 200)])
luxury_properties = len(df[df['price'] >= 200])

print()
print("MARKET SEGMENTATION:")
print("-" * 20)
print(f"💵 Budget Segment (<$100): {budget_properties} ({budget_properties/total_properties*100:.1f}%)")
print(f"💰 Mid-range Segment ($100-199): {midrange_properties} ({midrange_properties/total_properties*100:.1f}%)")
print(f"💎 Luxury Segment ($200+): {luxury_properties} ({luxury_properties/total_properties*100:.1f}%)")

print("\n" + "="*50 + "\n")

# ============================================================================
# 2. COMPETITIVE LANDSCAPE
# ============================================================================

print("=== 2. COMPETITIVE LANDSCAPE ===")
print()

# Analyze by neighborhood
neighborhood_analysis = df.groupby('neighborhood').agg({
    'price': ['count', 'mean', 'median'],
    'review_score': 'mean',
    'availability_365': 'mean'
}).round(2)

neighborhood_analysis.columns = ['Properties', 'Avg_Price', 'Median_Price', 'Avg_Rating', 'Avg_Availability']
neighborhood_analysis = neighborhood_analysis.sort_values('Avg_Price', ascending=False)

print("NEIGHBORHOOD PERFORMANCE:")
print("-" * 30)
print(neighborhood_analysis)

# Identify market leaders and opportunities
premium_neighborhood = neighborhood_analysis.index[0]
value_neighborhood = neighborhood_analysis.sort_values('Avg_Price').index[0]
highest_rated_neighborhood = neighborhood_analysis.sort_values('Avg_Rating', ascending=False).index[0]

print()
print("KEY FINDINGS:")
print("-" * 15)
print(f"🏆 Premium Market Leader: {premium_neighborhood}")
print(f"💡 Value Market Opportunity: {value_neighborhood}")
print(f"⭐ Highest Customer Satisfaction: {highest_rated_neighborhood}")

print("\n" + "="*50 + "\n")

# ============================================================================
# 3. PRODUCT MIX ANALYSIS
# ============================================================================

print("=== 3. PRODUCT MIX ANALYSIS ===")
print()

# Analyze by property type
property_analysis = df.groupby('property_type').agg({
    'price': ['count', 'mean', 'median'],
    'review_score': 'mean',
    'bedrooms': 'mean',
    'accommodates': 'mean'
}).round(2)

property_analysis.columns = ['Count', 'Avg_Price', 'Median_Price', 'Avg_Rating', 'Avg_Bedrooms', 'Avg_Capacity']

print("PROPERTY TYPE PERFORMANCE:")
print("-" * 30)
print(property_analysis)

# Calculate price per person for value analysis
df['price_per_person'] = df['price'] / df['accommodates']
value_analysis = df.groupby('property_type')['price_per_person'].mean().sort_values()

print()
print("VALUE PROPOSITION (Price per Person):")
print("-" * 35)
for prop_type, price_per_person in value_analysis.items():
    print(f"{prop_type}: ${price_per_person:.2f} per person")

print("\n" + "="*50 + "\n")

# ============================================================================
# 4. QUALITY AND CUSTOMER SATISFACTION
# ============================================================================

print("=== 4. QUALITY METRICS ===")
print()

# Quality distribution
quality_metrics = {
    'Excellent (4.7+)': len(df[df['review_score'] >= 4.7]),
    'Very Good (4.3-4.6)': len(df[(df['review_score'] >= 4.3) & (df['review_score'] < 4.7)]),
    'Good (4.0-4.2)': len(df[(df['review_score'] >= 4.0) & (df['review_score'] < 4.3)]),
    'Needs Improvement (<4.0)': len(df[df['review_score'] < 4.0])
}

print("QUALITY DISTRIBUTION:")
print("-" * 20)
for category, count in quality_metrics.items():
    percentage = (count / total_properties) * 100
    print(f"{category}: {count} properties ({percentage:.1f}%)")

# Correlation between quality and price
high_quality = df[df['review_score'] >= 4.5]
low_quality = df[df['review_score'] < 4.5]

print()
print("QUALITY-PRICE RELATIONSHIP:")
print("-" * 25)
print(f"High-rated properties (4.5+) average price: ${high_quality['price'].mean():.2f}")
print(f"Lower-rated properties (<4.5) average price: ${low_quality['price'].mean():.2f}")
price_premium = high_quality['price'].mean() - low_quality['price'].mean()
print(f"Quality premium: ${price_premium:.2f} ({price_premium/low_quality['price'].mean()*100:.1f}%)")

print("\n" + "="*50 + "\n")

# ============================================================================
# 5. BUSINESS OPPORTUNITIES
# ============================================================================

print("=== 5. STRATEGIC OPPORTUNITIES ===")
print()

# Identify undervalued high-quality properties
undervalued = df[(df['review_score'] >= 4.5) & (df['price'] < median_price)]
overpriced = df[(df['review_score'] < 4.0) & (df['price'] > median_price)]

print("PRICING OPPORTUNITIES:")
print("-" * 20)
print(f"🔍 Undervalued high-quality properties: {len(undervalued)}")
print(f"⚠️  Overpriced low-quality properties: {len(overpriced)}")

if len(undervalued) > 0:
    avg_undervalued_price = undervalued['price'].mean()
    potential_increase = median_price - avg_undervalued_price
    print(f"💡 Potential price increase for undervalued: ${potential_increase:.2f}")

# Market gaps analysis
print()
print("MARKET GAP ANALYSIS:")
print("-" * 20)

# Find underserved segments
bedroom_demand = df.groupby('bedrooms').size()
print("Properties by bedroom count:")
for bedrooms, count in bedroom_demand.items():
    print(f"  {bedrooms} bedroom(s): {count} properties")

# Identify gaps
if 5 not in bedroom_demand.index or bedroom_demand.get(5, 0) < 2:
    print("🎯 Opportunity: Large family properties (5+ bedrooms) are underrepresented")

print("\n" + "="*50 + "\n")

# ============================================================================
# 6. FINANCIAL PROJECTIONS
# ============================================================================

print("=== 6. FINANCIAL ANALYSIS ===")
print()

# Calculate ROI scenarios
investment_scenarios = {
    'Budget Property': {'investment': 50000, 'avg_price': df[df['price'] < 100]['price'].mean()},
    'Mid-range Property': {'investment': 100000, 'avg_price': df[(df['price'] >= 100) & (df['price'] < 200)]['price'].mean()},
    'Luxury Property': {'investment': 200000, 'avg_price': df[df['price'] >= 200]['price'].mean()}
}

print("INVESTMENT SCENARIOS:")
print("-" * 20)

for scenario, data in investment_scenarios.items():
    if not pd.isna(data['avg_price']):
        annual_revenue = data['avg_price'] * 250  # Assume 250 booked nights
        operating_costs = annual_revenue * 0.3   # Assume 30% operating costs
        net_income = annual_revenue - operating_costs
        roi = (net_income / data['investment']) * 100
        
        print(f"\n{scenario}:")
        print(f"  Initial Investment: ${data['investment']:,}")
        print(f"  Average Nightly Rate: ${data['avg_price']:.2f}")
        print(f"  Projected Annual Revenue: ${annual_revenue:,.0f}")
        print(f"  Net Annual Income: ${net_income:,.0f}")
        print(f"  ROI: {roi:.1f}%")

print("\n" + "="*50 + "\n")

# ============================================================================
# 7. RISK ANALYSIS
# ============================================================================

print("=== 7. RISK ASSESSMENT ===")
print()

# Market concentration risk
neighborhood_concentration = df['neighborhood'].value_counts()
top_neighborhood_share = neighborhood_concentration.iloc[0] / total_properties

print("MARKET RISKS:")
print("-" * 15)
print(f"📍 Geographic Concentration: {neighborhood_concentration.iloc[0]} properties ({top_neighborhood_share*100:.1f}%) in {neighborhood_concentration.index[0]}")

if top_neighborhood_share > 0.4:
    print("   ⚠️  HIGH RISK: Over-concentration in single neighborhood")
elif top_neighborhood_share > 0.3:
    print("   ⚠️  MEDIUM RISK: Moderate concentration risk")
else:
    print("   ✅ LOW RISK: Well-diversified geographic spread")

# Quality risk
low_quality_properties = len(df[df['review_score'] < 4.0])
quality_risk = low_quality_properties / total_properties

print()
print(f"⭐ Quality Risk: {low_quality_properties} properties ({quality_risk*100:.1f}%) below 4.0 rating")
if quality_risk > 0.2:
    print("   ⚠️  HIGH RISK: Significant portion of low-quality properties")
else:
    print("   ✅ LOW RISK: Most properties maintain good quality standards")

print("\n" + "="*50 + "\n")

# ============================================================================
# 8. STRATEGIC RECOMMENDATIONS
# ============================================================================

print("=== 8. STRATEGIC RECOMMENDATIONS ===")
print()

print("IMMEDIATE ACTIONS (0-3 months):")
print("-" * 35)

# Price optimization recommendations
if len(undervalued) > 0:
    revenue_opportunity = len(undervalued) * (median_price - undervalued['price'].mean()) * 250
    print(f"💰 PRICING: Increase prices on {len(undervalued)} undervalued properties")
    print(f"   Potential additional revenue: ${revenue_opportunity:,.0f} annually")

if len(overpriced) > 0:
    print(f"📉 PRICING: Review pricing on {len(overpriced)} overpriced properties")
    print(f"   Focus on improving quality or reducing prices")

print()
print("MEDIUM-TERM STRATEGY (3-12 months):")
print("-" * 38)

# Market expansion recommendations
underrepresented_neighborhoods = neighborhood_analysis.sort_values('Properties').head(2)
print(f"🌍 EXPANSION: Consider expansion in underrepresented areas:")
for neighborhood in underrepresented_neighborhoods.index:
    print(f"   • {neighborhood}: Only {underrepresented_neighborhoods.loc[neighborhood, 'Properties']:.0f} properties")

# Quality improvement
if quality_risk > 0.15:
    print(f"⭐ QUALITY: Implement quality improvement program")
    print(f"   Target: Bring all properties above 4.0 rating")

print()
print("LONG-TERM VISION (1+ years):")
print("-" * 28)
print("🎯 PORTFOLIO: Build diversified portfolio across all segments")
print("📊 DATA: Implement dynamic pricing based on demand patterns")
print("🤝 PARTNERSHIPS: Develop strategic partnerships with property owners")
print("🔄 OPTIMIZATION: Continuous market analysis and portfolio rebalancing")

print("\n" + "="*50 + "\n")

# ============================================================================
# 9. KEY PERFORMANCE INDICATORS (KPIs)
# ============================================================================

print("=== 9. RECOMMENDED KPIs FOR MONITORING ===")
print()

current_kpis = {
    'Average Daily Rate (ADR)': f"${avg_price:.2f}",
    'Occupancy Rate': f"{((365 - df['availability_365'].mean()) / 365)*100:.1f}%",
    'Revenue Per Available Room': f"${(avg_price * ((365 - df['availability_365'].mean()) / 365)):.2f}",
    'Average Review Score': f"{df['review_score'].mean():.2f}/5.0",
    'Properties Above 4.5 Rating': f"{len(df[df['review_score'] >= 4.5])}/{total_properties} ({len(df[df['review_score'] >= 4.5])/total_properties*100:.1f}%)",
    'Market Diversity Index': f"{len(df['neighborhood'].unique())} neighborhoods"
}

print("CURRENT PERFORMANCE:")
print("-" * 20)
for kpi, value in current_kpis.items():
    print(f"{kpi}: {value}")

print()
print("TARGET METRICS (Next 12 Months):")
print("-" * 35)
print("• Average Daily Rate: Increase by 10-15%")
print("• Occupancy Rate: Maintain above 70%")
print("• Average Review Score: Above 4.3")
print("• Quality Properties (4.5+): Above 60%")
print("• Market Expansion: Enter 2-3 new neighborhoods")

print("\n" + "="*50 + "\n")

# ============================================================================
# 10. EXECUTIVE SUMMARY
# ============================================================================

print("=== 10. EXECUTIVE SUMMARY ===")
print()

print("🎯 KEY FINDINGS:")
print("-" * 20)
print(f"• Market of {total_properties} properties with ${avg_price:.2f} average nightly rate")
print(f"• {premium_neighborhood} commands highest prices (premium segment)")
print(f"• {len(high_quality)} properties ({len(high_quality)/total_properties*100:.1f}%) rated 4.5+ stars")
print(f"• Market potential: ${total_potential_revenue:,.0f} annual revenue")

print()
print("💡 OPPORTUNITIES:")
print("-" * 20)
print(f"• {len(undervalued)} undervalued high-quality properties identified")
print(f"• Quality premium of ${price_premium:.2f} per night available")
print("• Geographic expansion opportunities in underserved areas")
print("• Product mix optimization potential")

print()
print("⚠️  RISKS TO MONITOR:")
print("-" * 20)
print(f"• Geographic concentration risk in {neighborhood_concentration.index[0]}")
print(f"• {low_quality_properties} properties with quality issues")
print("• Competitive pressure in premium segments")

print()
print("🚀 NEXT STEPS:")
print("-" * 15)
print("1. Implement pricing optimization for identified properties")
print("2. Develop quality improvement program")
print("3. Analyze expansion opportunities in detail")
print("4. Set up monthly KPI monitoring dashboard")
print("5. Conduct deeper market research on customer segments")

print("\n" + "="*60)
print("CONGRATULATIONS! 🎉")
print("You've completed a comprehensive business analysis!")
print("You now have the skills to:")
print("• Analyze data systematically")
print("• Identify business opportunities")
print("• Make data-driven recommendations")
print("• Present insights professionally")
print("="*60)

print()
print("Continue practicing with real datasets to master these skills!")
print("The journey from data to business insights is now yours to explore! 🚀")