import random
import os
import csv
from datetime import datetime

# Define the Orders folder path
orders_folder = r"c:\Users\shabnamwatson\OneDrive - ABI Cube\The Book\GitHub\SampleFiles\Orders"

# Read the 2021 data as template
template_file = os.path.join(orders_folder, "2021.csv")
template_rows = []

print("Reading template file (2021.csv)...")
with open(template_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    template_rows = list(reader)

print(f"Template has {len(template_rows)} rows")

# Generate files for 2022-2026 based on 2021 template
for year in range(2022, 2027):
    output_file = os.path.join(orders_folder, f"{year}.csv")
    
    print(f"\nGenerating {year}.csv...")
    
    # Copy template rows
    rows = [row[:] for row in template_rows]  # Deep copy
    
    # Update dates to the new year
    for row in rows:
        if len(row) > 2:
            try:
                # Parse the date and update the year
                old_date = row[2]
                # Assuming date format like "2021-07-01"
                date_parts = old_date.split('-')
                if len(date_parts) == 3:
                    date_parts[0] = str(year)
                    row[2] = '-'.join(date_parts)
            except:
                pass
    
    # Update Quantity column (index 6)
    for row in rows:
        if len(row) > 6:
            row[6] = str(random.randint(1, 10))
    
    # Randomly remove 5-10% of rows
    original_count = len(rows)
    random_percentage = random.uniform(0.05, 0.10)
    rows_to_remove = int(original_count * random_percentage)
    
    # Randomly select indices to remove
    indices_to_remove = set(random.sample(range(original_count), rows_to_remove))
    
    # Keep rows that are not in the removal list
    rows = [rows[i] for i in range(len(rows)) if i not in indices_to_remove]
    
    final_count = len(rows)
    removed_count = original_count - final_count
    removal_percentage = (removed_count / original_count) * 100
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"  Original rows: {original_count}")
    print(f"  Removed: {removed_count} rows ({removal_percentage:.2f}%)")
    print(f"  Final rows: {final_count}")
    print(f"  Successfully created: {year}.csv")

# Now process existing files (2019, 2020, 2021)
print("\n" + "="*50)
print("Processing existing files (2019-2021)...")
print("="*50)

for year in [2019, 2020, 2021]:
    csv_file = os.path.join(orders_folder, f"{year}.csv")
    
    print(f"\nProcessing: {year}.csv")
    
    # Read the CSV file
    rows = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    original_count = len(rows)
    print(f"Original row count: {original_count}")
    
    # Update Quantity column (index 6)
    for row in rows:
        if len(row) > 6:
            row[6] = str(random.randint(1, 10))
    
    # Randomly remove 5-10% of rows
    random_percentage = random.uniform(0.05, 0.10)
    rows_to_remove = int(original_count * random_percentage)
    
    # Randomly select indices to remove
    indices_to_remove = set(random.sample(range(original_count), rows_to_remove))
    
    # Keep rows that are not in the removal list
    rows = [rows[i] for i in range(len(rows)) if i not in indices_to_remove]
    
    final_count = len(rows)
    removed_count = original_count - final_count
    removal_percentage = (removed_count / original_count) * 100
    
    # Write back to file
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"Removed {removed_count} rows ({removal_percentage:.2f}%)")
    print(f"Final row count: {final_count}")
    print(f"Successfully updated: {year}.csv")

print("\n" + "="*50)
print("All files processed successfully!")
print("="*50)
