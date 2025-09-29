"""
Setup Test - Run this first!
=============================

This script tests that your Python environment is set up correctly
for the business data analysis tutorial.

Run this script before starting the main tutorial to ensure
everything is working properly.
"""

import sys

print("="*50)
print("PYTHON TUTORIAL SETUP TEST")
print("="*50)
print()

# Test 1: Python version
print("1. Testing Python Version...")
python_version = sys.version_info
print(f"   Python {python_version.major}.{python_version.minor}.{python_version.micro}")

if python_version.major >= 3 and python_version.minor >= 7:
    print("   ✅ Python version is compatible")
else:
    print("   ❌ Python 3.7+ required")
    print("   Please upgrade your Python installation")
    exit(1)

print()

# Test 2: Required packages
print("2. Testing Required Packages...")
required_packages = ['pandas', 'matplotlib', 'numpy']
missing_packages = []

for package in required_packages:
    try:
        __import__(package)
        print(f"   ✅ {package} installed")
    except ImportError:
        print(f"   ❌ {package} missing")
        missing_packages.append(package)

if missing_packages:
    print()
    print("   Missing packages detected!")
    print("   Please run: pip install -r requirements.txt")
    exit(1)

print()

# Test 3: Data file
print("3. Testing Data File...")
try:
    import pandas as pd
    df = pd.read_csv('data/airbnb_sample.csv')
    print(f"   ✅ Sample data loaded successfully ({len(df)} rows)")
except FileNotFoundError:
    print("   ❌ Data file not found")
    print("   Make sure 'data/airbnb_sample.csv' exists")
    exit(1)
except Exception as e:
    print(f"   ❌ Error reading data: {e}")
    exit(1)

print()

# Test 4: Basic calculations
print("4. Testing Python Basics...")
try:
    # Basic arithmetic
    result = 150 * 0.08
    assert result == 12.0
    
    # String operations
    text = "  HELLO WORLD  "
    clean_text = text.strip().title()
    assert clean_text == "Hello World"
    
    # List operations
    prices = [100, 150, 200]
    average = sum(prices) / len(prices)
    assert average == 150.0
    
    print("   ✅ Python basics working correctly")
except Exception as e:
    print(f"   ❌ Basic operations failed: {e}")
    exit(1)

print()

# Test 5: Matplotlib (basic chart creation)
print("5. Testing Visualization...")
try:
    import matplotlib.pyplot as plt
    # Create a simple test plot (don't display it)
    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3], [1, 4, 2])
    plt.close()  # Close without displaying
    print("   ✅ Matplotlib working correctly")
except Exception as e:
    print(f"   ❌ Visualization test failed: {e}")
    print("   Charts may not work properly")

print()

# Final results
print("="*50)
print("SETUP TEST COMPLETE")
print("="*50)
print()
print("🎉 All tests passed! You're ready to start learning.")
print()
print("NEXT STEPS:")
print("-" * 15)
print("1. Read GETTING_STARTED.md for the learning path")
print("2. Start with: python 01_python_basics.py")
print("3. Follow the modules in order (01 → 02 → 03 → ...)")
print("4. Try the exercises when you're ready")
print()
print("Happy learning! 🚀")
print("="*50)