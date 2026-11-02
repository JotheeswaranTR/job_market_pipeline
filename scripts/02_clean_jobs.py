import pandas as pd
import re

# 1. Load the raw data
print("Loading raw data...")
df = pd.read_csv("data/raw_jobs.csv")
print(f"Rows BEFORE cleaning: {len(df)}")

# 2. Remove duplicates based on title and company
df = df.drop_duplicates(subset=["title", "company"])

# 3. Handle missing values
# Fill missing text with 'Unknown' so Pandas doesn't break
df["company"] = df["company"].fillna("Unknown")
df["location"] = df["location"].fillna("Unknown")
df["description"] = df["description"].fillna("")

# 4. Clean the description text
# This is a small function to strip HTML tags and extra spaces
def clean_text(text):
    text = str(text)
    text = re.sub(r'<[^>]+>', ' ', text)  # Replace HTML tags with a space
    text = re.sub(r'\s+', ' ', text)      # Replace multiple spaces with one space
    return text.strip()

print("Cleaning HTML tags from descriptions...")
df["description"] = df["description"].apply(clean_text)

# Normalize basic text (lowercase for consistency)
df["title"] = df["title"].str.lower().str.strip()
df["location"] = df["location"].str.lower().str.strip()

print(f"Rows AFTER cleaning: {len(df)}")

# 5. Save to the new cleaned file
output_path = "data/cleaned_jobs.csv"
df.to_csv(output_path, index=False)
print(f"Saved cleaned data to {output_path}")