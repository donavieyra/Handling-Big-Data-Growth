import csv
import gzip
import os
import pandas as pd

# Load dataset:
df = pd.read_csv("netflix_titles.csv")

# Step 1: Trim whitespace and remove empty rows:
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.dropna(how="all", inplace=True)

# Step 2: Remove duplicate rows:
df.drop_duplicates(inplace=True)

# Save cleaned dataset:
df.to_csv("netflix_clean.csv", index=False)

# Step 3: Compress the cleaned dataset using gzip:
with open("netflix_clean.csv", "rb") as f_in:
    with gzip.open("netflix_clean.csv.gz", "wb") as f_out:
        f_out.writelines(f_in)

# Show file sizes before and after:
original_size = os.path.getsize("netflix_titles.csv") / 1024
cleaned_size = os.path.getsize("netflix_clean.csv") / 1024
compressed_size = os.path.getsize("netflix_clean.csv.gz") / 1024

print(f"Original size   : {original_size:.2f} KB")
print(f"Cleaned size    : {cleaned_size:.2f} KB")
print(f"Compressed size : {compressed_size:.2f} KB")
