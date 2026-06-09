# Job Market Analytics Dashboard (End-to-End Project)
This project is an end-to-end **Job Market Analytics** solution built with **Python, SQL, Power BI, Streamlit, and VS Code**. It analyzes job postings to uncover insights about **salaries, in-demand skills, cities, experience levels, and job types (Remote / Hybrid / Onsite)**. It also includes an **AI chatbot** that answers questions about the same dataset.

## 🎯 Objectives
- Understand **which skills** are most in demand for data roles.
- Analyze **salary trends** by city, job type, and experience level.
- Compare **Remote vs Hybrid vs Onsite** job distribution.
- Identify **top hiring cities and companies**.
- Build an **interactive Power BI dashboard** for stakeholders.
- Create an **AI-powered chatbot** to answer questions about the job market.
- Practice working with **VS Code + Jupyter + Power BI + Streamlit** together in one project.

## 🧰 Tech Stack
- **Python** (Pandas, NumPy)
- **SQLite** (via SQLAlchemy)
- **Jupyter Notebooks** (data cleaning and analysis)
- **Power BI Desktop** (dashboard)
- **Streamlit** (chatbot web app)
- **Visual Studio Code (VS Code)** for editing `.py` files and managing the project

## 🗂 Project Structure
```text
Job_Market_Analytics/
├── data
│   ├── raw/                 # Original / sample job postings dataset
│   └── cleaned/             # Cleaned datasets (e.g., data_analyst_jobs.csv)
├── database/
│   └── job_market.db        # SQLite database
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_analysis.ipynb
│   ├── 04_sql_database.ipynb
│   └── 05_export_powerbi.ipynb
├── output/
│   ├── job_market_for_powerbi.csv   # Main dataset for Power BI
│   ├── overall_metrics.csv
│   ├── skills_summary.csv
│   ├── city_summary.csv
│   ├── experience_summary.csv
│   ├── job_type_summary.csv
│   └── monthly_trend.csv
├── src/
│   └── chatbot_app.py        # Streamlit chatbot application (created in VS Code)
|__screenshots
|___pbix file
└── README.md
```
> **Note:** All relative paths are set assuming the **project root folder is `Job_Market_Analytics`**, Jupyter notebooks live in `/notebooks`, and code files live in `/src`.
## 🔄 End-to-End Workflow

### 1️⃣ Data Cleaning & Preparation (Jupyter)
**Tools:** Jupyter Notebook (inside VS Code or standalone)
1. Open the project in VS Code or directly open the notebooks.
2. Use `02_data_cleaning.ipynb` to:
   - Load the raw dataset from `data/raw/`.
   - Clean and standardize:
     - `job_title_clean`
     - `location_clean`
     - `posted_date`
     - `salary_min`, `salary_max`, and `salary_avg`
     - Skill flags (Python, SQL, Power BI, etc.)
   - Filter to relevant roles (e.g., data-focused jobs).
3. Save cleaned data to:
```text
data/cleaned/data_analyst_jobs.csv
```
> Relative paths inside notebooks use `../` because notebooks are in `/notebooks` and data is in `/data`.
---
### 2️⃣ SQL Database Creation (SQLite)
**Tools:** Jupyter Notebook + SQLAlchemy
Notebook: `04_sql_database.ipynb`
- Loads:
```python
df = pd.read_csv('../data/cleaned/data_analyst_jobs.csv')
```
- Ensures the `database` folder exists:
``python
os.makedirs('../database', exist_ok=True)
```
- Creates a SQLite database and engine:
```python
engine = create_engine('sqlite:///../database/job_market.db')
```
- Writes the cleaned data into a `jobs` table:
```python
df.to_sql('jobs', engine, if_exists='replace', index=False)
```
- Runs sample SQL queries (total jobs, salary by experience level, jobs by city) to validate data.
> All paths were **re-edited** to use correct relative locations from the `/notebooks` folder.
---
### 3️⃣ Export for Power BI (Jupyter)
**Tools:** Jupyter Notebook
Notebook: `05_export_powerbi.ipynb`
This notebook:
1. Loads cleaned data:
```python
df = pd.read_csv('../data/cleaned/data_analyst_jobs.csv')
```
2. Creates multiple summary tables:
   - Overall metrics (`overall_metrics.csv`)
   - Skills summary (`skills_summary.csv`)
   - City summary (`city_summary.csv`)
   - Experience summary (`experience_summary.csv`)
   - Job type summary (`job_type_summary.csv`)
   - Monthly trend (`monthly_trend.csv`)
3. Saves them to the `output/` folder:
```python
output_dir = os.path.join(base_dir, "output")
os.makedirs(output_dir, exist_ok=True)
df.to_csv(os.path.join(output_dir, "job_market_for_powerbi.csv"), index=False)
```
> All paths in this notebook were **re-edited** to use `../data/cleaned` and `../output` from inside `/notebooks`.
---
### 4️⃣ Power BI Dashboard
**Tools:** Power BI Desktop
Loaded from:
- Main table: `output/job_market_for_powerbi.csv`
- Supporting tables: `output/overall_metrics.csv`, `skills_summary.csv`, etc.
**Key visuals included:**
- **KPI Cards:**
  - Total Jobs
  - Average Salary
  - Total Cities
  - Total Companies
- **Charts:**
  - Jobs Trend by Month
  - Top Skills in Demand
  - Job Type Distribution (Remote / Onsite / Hybrid)
  - Jobs by City
  - Average Salary by Experience Level
  - Experience Level vs Job Type
  - Top Hiring Companies
- **Slicers:**
  - Experience Level
  - Job Type
  - City
All visuals are connected to slicers so users can interactively filter the job market.
---
## 🧠 AI Chatbot (Streamlit) – Built with VS Code
The chatbot is implemented in `src/chatbot_app.py` and was created/edited using **VS Code**.
### Files and Paths
- Chatbot code: `src/chatbot_app.py`
- Data source: `data/cleaned/data_analyst_jobs.csv`
- Project root: `Job_Market_Analytics/`
The code uses:
```python
DATA_PATH = "data/cleaned/data_analyst_jobs.csv"
df = pd.read_csv(DATA_PATH)
```
> Here, we run Streamlit from the **project root**, so the relative path `data/cleaned/...` is correct.
### How to Edit in VS Code (Beginner Friendly)
1. Open **VS Code**.
2. Go to **File → Open Folder…**.
3. Choose:  
   `C:\Users\yelle\Job_Market_Analytics`
4. In the left Explorer:
   - Right–click on `src` → **New File** → `chatbot_app.py`.
   - Paste the chatbot code (logic + Streamlit UI).
5. Save the file.
### How to Run the Chatbot
In **Command Prompt** or VS Code terminal:
```bash
cd C:\Users\yelle\Job_Market_Analytics
streamlit run src\chatbot_app.py
```
Then open the URL shown (usually `http://localhost:8501`).
### What the Chatbot Can Answer
- “What is the average salary?”
- “What is the average salary for entry level roles?”
- “How many remote jobs are there?”
- “What are the top skills in demand?”
- “Which cities have the most jobs?”
- “Which companies are hiring the most?”
Internally, it
- Parses the question in Python.
- Chooses the right calculation (salary, skills, city, experience, job type).
- Returns a clear, human‑friendly answer based on **your dataset only**.
---
## 📊 Example Insights
*(Adjust these based on your actual data.)*
- **Top Skills:** Python, SQL, and Power BI appear most frequently in job descriptions.
- **Top Cities:** Bangalore and Hyderabad have the highest number of job postings.
- **Experience:** Mid-level roles show the highest average salaries.
- **Job Types:** Remote and Hybrid roles form a significant part of the job market.
- **Companies:** A handful of companies contribute the majority of job postings.
---
## 🚀 How to Run Everything (Step-by-Step)
### 1. Set Up Environment
```bash
pip install pandas numpy streamlit sqlalchemy
```
### 2. Run Notebooks (in Jupyter)
1. `02_data_cleaning.ipynb` → creates `data/cleaned/data_analyst_jobs.csv`.
2. `04_sql_database.ipynb` → creates `database/job_market.db` using:
   ```python
   engine = create_engine('sqlite:///../database/job_market.db')
   ```
3. `05_export_powerbi.ipynb` → creates all CSVs in `output/`.
### 3. Build Dashboard (Power BI Desktop)
- Open **Power BI Desktop**.
- Use **Get Data → Text/CSV**.
- Load `output/job_market_for_powerbi.csv` and other summary files.
- Recreate/refresh the visuals.
### 4. Run Chatbot (Streamlit + VS Code)
```bash
cd Job_Market_Analytics
streamlit run src\chatbot_app.py
```
Ask questions in the browser UI.
## 📌 Future Improvements
- Hook the chatbot to an external LLM (e.g., OpenAI) to rephrase answers while still using your dataset for facts.
- Deploy the Streamlit app to the cloud (Streamlit Community Cloud, Render, etc.).
- Connect Power BI directly to the SQLite database for live refresh.
- Add more advanced analytics (e.g., salary prediction models).
## 🙋‍♀️ About This Project
This project was created as a **learning and portfolio project**, focusing on:
- Cleaning and transforming real‑world job data.
- Using Jupyter and VS Code together effectively.
- Building a professional Power BI dashboard.
- Creating a **data‑aware AI chatbot** in Streamlit.
- Managing an end‑to‑end workflow with correct paths and folders.
