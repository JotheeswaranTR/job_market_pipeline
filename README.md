# 📊 Automated Job Market Intelligence Pipeline
**Author:** Jotheeswaran TR | https://www.linkedin.com/in/jotheeswaran-tr/
## 📌 Problem Statement
The data analyst job market is highly competitive and constantly changing. Which skills are actually in demand? This project is an end-to-end Python pipeline that fetches live Data Analyst job postings from the Adzuna API, cleans the data, extracts required skills using Regex, and generates automated visual reports.

## 🏗️ Architecture
API (Adzuna) -> Fetch (Requests) -> Clean (Pandas) -> Analyze (Regex) -> Visualize (Seaborn) -> Export (CSV & PNG)

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Manipulation:** Pandas
- **API & Security:** Requests, python-dotenv
- **Text Processing:** Regex (re)
- **Visualization:** Matplotlib, Seaborn

## 🚀 How to Run
1. Clone this repo.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac)
4. Install dependencies: `pip install -r requirements.txt`
5. Add your Adzuna API keys to a `.env` file in the root directory:
   ```text
   ADZUNA_APP_ID=your_id
   ADZUNA_APP_KEY=your_key
6. Run the pipeline scripts in order:

   - `python scripts/01_fetch_jobs.py`
   - `python scripts/02_clean_jobs.py`
   - `python scripts/03_analyze_jobs.py`
   - `python scripts/04_visualize_jobs.py` 

💡 Key Insights
(Based on the latest run of the pipeline)

Top Skill: Python and SQL are tied for the most in-demand skills, followed by Excel.

Top Location: Bangalore is the leading hub for these roles.

Skill Pairing: Data from the co-occurrence heatmap shows that jobs asking for Python frequently also ask for SQL.

> **Note on Data Limitations:** Adzuna's free API limits job descriptions to short snippets (approx. 500 characters). This limits the number of skills we can extract. In a production environment, this pipeline is built to easily scale to full-length job descriptions.

📈 Visualizations
Top Skills
https://outputs/charts/01_top_skills.png

Top Locations
https://outputs/charts/02_top_locations.png

Skill Co-occurrence
https://outputs/charts/03_skill_cooccurrence.png   


---
*Built by Jotheeswaran TR. Data Sources: [Adzuna API](https://developer.adzuna.com/) and [RemoteOK API](https://remoteok.com/api).*
