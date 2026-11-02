import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

BASE_URL = "https://api.adzuna.com/v1/api/jobs/in/search/1"
params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 50,
    "what": "data analyst",
    "content-type": "application/json"
}

print("Fetching data from Adzuna...")
response = requests.get(BASE_URL, params=params, timeout=15)
response.raise_for_status() # Automatically throws an error if the request fails

data = response.json()
jobs = data.get("results", [])

# Extract only the fields we need into a list of dictionaries
rows = []
for job in jobs:
    rows.append({
        "title": job.get("title"),
        "company": job.get("company", {}).get("display_name"),
        "location": job.get("location", {}).get("display_name"),
        "description": job.get("description"),
        "redirect_url": job.get("redirect_url"),
        "created": job.get("created")
    })

# Convert to a Pandas DataFrame and save to CSV
df = pd.DataFrame(rows)
output_path = "data/raw_jobs.csv"
df.to_csv(output_path, index=False)

print(f"Successfully saved {len(df)} jobs to {output_path}")