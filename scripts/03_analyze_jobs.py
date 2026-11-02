import pandas as pd
import re

df = pd.read_csv("data/cleaned_jobs.csv")

SKILL_PATTERNS = {
    "SQL": r"\bsql\b", "Python": r"\bpython\b", "Power BI": r"\bpower\s?bi\b",
    "Tableau": r"\btableau\b", "Excel": r"\bexcel\b", "AWS": r"\baws\b",
    "Azure": r"\bazure\b", "R": r"\br\b", "SAS": r"\bsas\b", "Snowflake": r"\bsnowflake\b"
}

def extract_skills(row):
    text_lower = (str(row["title"]) + " " + str(row["description"])).lower()
    found_skills = []
    for skill_name, pattern in SKILL_PATTERNS.items():
        if re.search(pattern, text_lower):
            found_skills.append(skill_name)
    return ", ".join(found_skills)

df["skills"] = df.apply(extract_skills, axis=1)

# ---------------------------------------------------------
# ANALYSIS 1: Top Skills
# ---------------------------------------------------------
# Split the "SQL, Excel, Python" string into a flat list of words
all_skills = df["skills"].str.split(", ").explode()
# Remove empty strings
all_skills = all_skills[all_skills != ""] 
top_skills = all_skills.value_counts()

print("\n--- TOP 10 IN-DEMAND SKILLS ---")
print(top_skills.head(10))

# ---------------------------------------------------------
# ANALYSIS 2: Location Demand
# ---------------------------------------------------------
# Clean up location strings (e.g., keep just the city name)
top_locations = df["location"].value_counts().head(5)

print("\n--- TOP 5 LOCATIONS ---")
print(top_locations)

# ---------------------------------------------------------
# SAVE: Save the final dataset with the new 'skills' column
# ---------------------------------------------------------
df.to_csv("data/cleaned_jobs.csv", index=False)
print("\nSuccessfully updated data/cleaned_jobs.csv with skill data!")