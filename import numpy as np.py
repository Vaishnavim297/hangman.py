import numpy as np

# Step 1: Initialize 2D Array (Rows = Items, Columns = Days)
inventory = np.array([
    [50,  45,  55,  40,  35],   # Widget A
    [120, 115, 110, 105, 100],  # Widget B
    [15,  18,  12,  8,   22]    # Widget C
])

print("--- STEP 1: RAW INVENTORY MATRIX ---")
print(inventory)

# Step 2: Axis Analysis
# axis=1 calculates across the rows (for each item)
min_per_item = np.min(inventory, axis=1) 
# axis=0 calculates down the columns (for each day)
total_per_day = np.sum(inventory, axis=0)  

print("\n--- STEP 2: METRICS EXTRACED ---")
print(f"Lowest stock reached for each item: {min_per_item}")
print(f"Total warehouse units per day:     {total_per_day}")

# Step 3: Threshold Filtering
CRITICAL_LEVEL = 20
# Creates a True/False matrix matching the shape of 'inventory'
low_stock_mask = inventory < CRITICAL_LEVEL 

print("\n--- STEP 3: CRITICAL ALERTS ---")
print("Days/Items requiring immediate restock (True):")
print(low_stock_mask)
print(f"Exact low-stock values found: {inventory[low_stock_mask]}")