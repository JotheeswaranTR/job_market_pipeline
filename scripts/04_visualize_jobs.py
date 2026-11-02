import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

SKILL_PATTERNS = {
    "SQL": r"\bsql\b", "Python": r"\bpython\b", "Power BI": r"\bpower\s?bi\b",
    "Tableau": r"\btableau\b", "Excel": r"\bexcel\b", "AWS": r"\baws\b",
    "Azure": r"\bazure\b", "R": r"\br\b", "SAS": r"\bsas\b", "Snowflake": r"\bsnowflake\b"
}

# Ensure the output directory exists
os.makedirs("outputs/charts", exist_ok=True)

# Set a nice visual style for Seaborn
sns.set_theme(style="whitegrid")

# Load the data
df = pd.read_csv("data/cleaned_jobs.csv")

# 1. Prepare the skill data
all_skills = df["skills"].str.split(", ").explode()
all_skills = all_skills[all_skills != ""]
top_skills = all_skills.value_counts().head(10)

# 2. Create the plot
plt.figure(figsize=(10, 6)) # 10 inches wide, 6 inches tall
sns.barplot(x=top_skills.values, y=top_skills.index, hue=top_skills.index, palette="viridis", legend=False)

# 3. Add labels and title
plt.title("Top 10 In-Demand Skills for Data Analysts", fontsize=16, fontweight="bold")
plt.xlabel("Number of Job Postings", fontsize=12)
plt.ylabel("Skill", fontsize=12)


# 4. Save the chart
plt.tight_layout() # Ensures labels don't get cut off
plt.savefig("outputs/charts/01_top_skills.png")
print("Saved chart 1: outputs/charts/01_top_skills.png")

# Show the plot (optional, will pop up in a window)
# plt.show() 


# ---------------------------------------------------------
# CHART 2: Location-wise Demand
# ---------------------------------------------------------
# Extract just the first part of the location (the city)
df["city"] = df["location"].apply(lambda x: str(x).split(",")[0].strip().title())
top_locations = df["city"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.values, y=top_locations.index, hue=top_locations.index, palette="magma", legend=False)
plt.title("Top 10 Locations for Data Analyst Jobs", fontsize=16, fontweight="bold")
plt.xlabel("Number of Job Postings", fontsize=12)
plt.ylabel("City", fontsize=12)

plt.tight_layout()
plt.savefig("outputs/charts/02_top_locations.png")
print("Saved chart 2: outputs/charts/02_top_locations.png")
plt.close() # Clears the canvas for the next chart

# ---------------------------------------------------------
# CHART 3: Skill Co-occurrence Heatmap
# ---------------------------------------------------------
# We create a binary matrix: 1 if the job has the skill, 0 if not
skills_list = list(SKILL_PATTERNS.keys())
co_matrix = pd.DataFrame(0, index=df.index, columns=skills_list)

for skill in skills_list:
    # Check if the skill exists in the job's skill string
    co_matrix[skill] = df["skills"].apply(lambda x: 1 if skill in str(x) else 0)

# Calculate correlation (how often they appear together)
co_occurrence = co_matrix.T.dot(co_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(co_occurrence, annot=True, cmap="Blues", fmt="d", linewidths=.5)
plt.title("Skill Co-occurrence (How often skills appear together)", fontsize=16, fontweight="bold")

plt.tight_layout()
plt.savefig("outputs/charts/03_skill_cooccurrence.png")
print("Saved chart 3: outputs/charts/03_skill_cooccurrence.png")
plt.close()