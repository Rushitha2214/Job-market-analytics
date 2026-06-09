import streamlit as st
import pandas as pd
import numpy as np

# ========= CONFIG =========
DATA_PATH = "data/cleaned/data_analyst_jobs.csv"

st.set_page_config(
    page_title="Job Market Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========= CUSTOM CSS =========
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #0f1117;
    color: #e2e8f0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #1a1d27 !important;
    border-right: 1px solid #2d3148;
}

[data-testid="stSidebar"] * {
    color: #cbd5e1 !important;
}

/* ── Metric Cards ── */
.metric-card {
    background: linear-gradient(135deg, #1e2235 0%, #252a3d 100%);
    border: 1px solid #2d3357;
    border-radius: 12px;
    padding: 14px 18px;
    margin: 8px 0;
    transition: border-color 0.2s;
}
.metric-card:hover { border-color: #6366f1; }
.metric-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748b !important;
    margin-bottom: 4px;
}
.metric-value {
    font-size: 22px;
    font-weight: 700;
    color: #a5b4fc !important;
    line-height: 1.2;
}
.metric-sub {
    font-size: 11px;
    color: #475569 !important;
    margin-top: 2px;
}

/* ── Suggested chips ── */
.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin: 6px 0 12px 0;
}
.chip {
    background: #1e2235;
    border: 1px solid #2d3357;
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 12px;
    color: #94a3b8;
    cursor: pointer;
    white-space: nowrap;
}

/* ── Chat bubbles ── */
.chat-row {
    display: flex;
    margin: 10px 0;
    align-items: flex-start;
    gap: 10px;
}
.chat-row.user { justify-content: flex-end; }

.avatar {
    width: 34px; height: 34px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
}
.avatar.bot { background: #312e81; }
.avatar.user-av { background: #1e3a5f; }

.bubble {
    max-width: 76%;
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 14px;
    line-height: 1.6;
    color: #e2e8f0;
}
.bubble.bot {
    background: #1e2235;
    border: 1px solid #2d3357;
    border-top-left-radius: 4px;
}
.bubble.user {
    background: linear-gradient(135deg, #3730a3, #4338ca);
    border-top-right-radius: 4px;
}

.bubble-title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: #818cf8;
    margin-bottom: 6px;
}

/* ── Hero Header ── */
.hero {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #0f172a 100%);
    border: 1px solid #2d3357;
    border-radius: 16px;
    padding: 28px 32px 22px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-tag {
    display: inline-block;
    background: rgba(99,102,241,0.15);
    border: 1px solid rgba(99,102,241,0.3);
    color: #a5b4fc;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 12px;
}
.hero h1 {
    font-size: 26px !important;
    font-weight: 700 !important;
    color: #f1f5f9 !important;
    margin: 0 0 8px !important;
    line-height: 1.25 !important;
}
.hero p {
    color: #64748b;
    font-size: 14px;
    margin: 0;
}

/* ── Input box ── */
[data-testid="stChatInput"] textarea {
    background: #1a1d27 !important;
    border: 1px solid #2d3357 !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
}

/* ── Dividers ── */
hr { border-color: #1e2235 !important; }

/* ── Section label ── */
.section-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #475569;
    margin: 16px 0 8px;
}

/* ── Status dot ── */
.status-dot {
    display: inline-block;
    width: 7px; height: 7px;
    background: #22c55e;
    border-radius: 50%;
    margin-right: 6px;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Fix white space around chat input ── */
[data-testid="stBottom"] {
    background: #0f1117 !important;
    border-top: 1px solid #1e2235 !important;
}

[data-testid="stBottom"] > div {
    background: #0f1117 !important;
}

.stChatFloatingInputContainer {
    background: #0f1117 !important;
    border-top: 1px solid #1e2235 !important;
    padding-bottom: 12px !important;
}
</style>
""", unsafe_allow_html=True)


# ========= LOAD DATA =========
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    if "salary_avg" not in df.columns:
        if {"salary_min", "salary_max"}.issubset(df.columns):
            df["salary_avg"] = (df["salary_min"] + df["salary_max"]) / 2
    if "location_clean" not in df.columns and "location" in df.columns:
        df["location_clean"] = df["location"].str.title().str.strip()
    return df

df = load_data(DATA_PATH)


# ========= HELPER FUNCTIONS =========

def get_top_skills(df, top_n=5):
    skill_cols = [
        "Python", "SQL", "Excel", "Power BI", "Tableau", "Machine Learning",
        "TensorFlow", "AWS", "Azure", "R", "JavaScript", "DAX", "Visualization"
    ]
    existing = [c for c in skill_cols if c in df.columns]
    if not existing:
        return []
    counts = df[existing].sum().sort_values(ascending=False)
    return list(zip(counts.index[:top_n], counts.values[:top_n]))

def get_jobs_by_city(df):
    if "location_clean" not in df.columns:
        return None
    return (
        df.groupby("location_clean")
          .agg(job_count=("job_id", "count"), avg_salary=("salary_avg", "mean"))
          .sort_values("job_count", ascending=False)
    )

def generate_structured_answer(question, df):
    q = question.lower()
    total_jobs = len(df)
    avg_salary = df["salary_avg"].mean() if "salary_avg" in df.columns else None

    if any(w in q for w in ["salary", "pay", "ctc", "package"]):
        if "entry" in q:
            subset = df[df["experience_level"].str.contains("Entry", case=False, na=False)]
        elif "mid" in q:
            subset = df[df["experience_level"].str.contains("Mid", case=False, na=False)]
        elif "senior" in q:
            subset = df[df["experience_level"].str.contains("Senior", case=False, na=False)]
        else:
            subset = df
        if len(subset) == 0:
            return "Salary Insights", "No matching jobs found for that experience level."
        return (
            "Salary Insights",
            f"For the selected roles, the **average salary** is around ₹{subset['salary_avg'].mean():,.0f} "
            f"and the **median salary** is about ₹{subset['salary_avg'].median():,.0f}."
        )

    if any(w in q for w in ["remote", "hybrid", "onsite", "work from home", "wfh"]):
        if "job_type" not in df.columns:
            return "Job Type Distribution", "Job type information is not available in the dataset."
        counts = df["job_type"].value_counts()
        total = counts.sum()
        parts = [f"**{jt}** — {c} jobs ({c/total*100:.1f}%)" for jt, c in counts.items()]
        return "Job Type Distribution", "Here is the breakdown of job types:\n\n" + "\n\n".join(f"• {p}" for p in parts)

    if any(w in q for w in ["skill", "skills", "demand", "top skills"]):
        top_skills = get_top_skills(df, top_n=5)
        if not top_skills:
            return "Skills in Demand", "Skill columns are not present in the dataset."
        lines = [f"{i+1}. **{skill}** — required in {int(count)} job postings" for i, (skill, count) in enumerate(top_skills)]
        return "Skills in Demand", "Top skills based on current job postings:\n\n" + "\n\n".join(lines)

    if any(w in q for w in ["city", "location", "where", "which city"]):
        city_stats = get_jobs_by_city(df)
        if city_stats is None:
            return "City Insights", "City information is not available."
        lines = [f"• **{city}** — {int(row.job_count)} jobs, avg ₹{row.avg_salary:,.0f}" for city, row in city_stats.head(5).iterrows()]
        return "City Insights", "Top cities by number of job postings:\n\n" + "\n\n".join(lines)

    if any(w in q for w in ["experience", "entry", "senior", "mid"]):
        if "experience_level" not in df.columns:
            return "Experience Insights", "Experience level information is missing."
        stats = df.groupby("experience_level").agg(job_count=("job_id", "count"), avg_salary=("salary_avg", "mean")).sort_values("avg_salary", ascending=False)
        lines = [f"• **{lvl}** — {int(row.job_count)} jobs, avg ₹{row.avg_salary:,.0f}" for lvl, row in stats.iterrows()]
        return "Experience Breakdown", "Salary and job count by experience level:\n\n" + "\n\n".join(lines)

    if any(w in q for w in ["company", "companies", "hiring"]):
        if "company" not in df.columns:
            return "Company Insights", "Company information is not available."
        comp_stats = df.groupby("company").agg(job_count=("job_id", "count")).sort_values("job_count", ascending=False).head(5)
        lines = [f"• **{company}** — {int(row.job_count)} postings" for company, row in comp_stats.iterrows()]
        return "Top Hiring Companies", "Companies with the most open roles:\n\n" + "\n\n".join(lines)

    avg_str = f"₹{avg_salary:,.0f}" if avg_salary else "N/A"
    return (
        "Overview",
        f"The dataset contains **{total_jobs:,} job postings** with an average salary of **{avg_str}**.\n\n"
        "Try asking:\n\n"
        "• What is the average salary for entry level roles?\n\n"
        "• Which cities have the most data analyst jobs?\n\n"
        "• What are the top skills in demand?\n\n"
        "• Show me remote vs onsite job distribution\n\n"
        "• Which companies are hiring the most?"
    )


# ========= SIDEBAR =========
with st.sidebar:
    st.markdown('<div class="section-label">Dataset Overview</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Job Postings</div>
        <div class="metric-value">{len(df):,}</div>
        <div class="metric-sub">across all experience levels</div>
    </div>""", unsafe_allow_html=True)

    if "salary_avg" in df.columns:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Average Salary</div>
            <div class="metric-value">₹{df['salary_avg'].mean():,.0f}</div>
            <div class="metric-sub">median ₹{df['salary_avg'].median():,.0f}</div>
        </div>""", unsafe_allow_html=True)

    if "location_clean" in df.columns:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Cities Covered</div>
            <div class="metric-value">{df['location_clean'].nunique()}</div>
            <div class="metric-sub">unique locations</div>
        </div>""", unsafe_allow_html=True)

    if "company" in df.columns:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Hiring Companies</div>
            <div class="metric-value">{df['company'].nunique()}</div>
            <div class="metric-sub">unique employers</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-label" style="margin-top:20px;">Quick Filters</div>', unsafe_allow_html=True)

    if "experience_level" in df.columns:
        levels = sorted(df["experience_level"].dropna().unique())
        for lvl in levels:
            count = len(df[df["experience_level"] == lvl])
            pct = count / len(df) * 100
            st.markdown(f"""
            <div style="display:flex; justify-content:space-between; align-items:center;
                        padding:6px 0; border-bottom:1px solid #1e2235; font-size:13px;">
                <span style="color:#94a3b8;">{lvl}</span>
                <span style="color:#6366f1; font-weight:600;">{count} <span style="color:#475569; font-weight:400;">({pct:.0f}%)</span></span>
            </div>""", unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:11px; color:#334155; text-align:center;">Job Market Intelligence v1.0<br>Built with Streamlit · Python · Pandas</div>', unsafe_allow_html=True)


# ========= MAIN AREA =========

# Hero header
st.markdown("""
<div class="hero">
    <div class="hero-tag">📊 Live Dataset Analysis</div>
    <h1>Job Market Intelligence</h1>
    <p>Ask anything about salaries, top skills, hiring cities, experience levels, and more — powered by real job posting data.</p>
</div>
""", unsafe_allow_html=True)

# Suggested questions chips
st.markdown("""
<div class="section-label">Suggested Questions</div>
<div class="chip-row">
  <span class="chip">💰 Average salary for entry level</span>
  <span class="chip">🏙️ Top cities for data analyst jobs</span>
  <span class="chip">🛠️ Most in-demand skills</span>
  <span class="chip">🏢 Which companies are hiring?</span>
  <span class="chip">📶 Remote vs onsite split</span>
</div>
""", unsafe_allow_html=True)

# Chat history init
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="chat-row user">
            <div class="bubble user">{msg["content"]}</div>
            <div class="avatar user-av">👤</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        title = msg.get("title", "")
        content = msg["content"]
        st.markdown(f"""
        <div class="chat-row">
            <div class="avatar bot">🤖</div>
            <div class="bubble bot">
                <div class="bubble-title">{title}</div>
                {content}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Input
user_question = st.chat_input("Ask about salaries, skills, cities, experience levels...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})

    title, answer = generate_structured_answer(user_question, df)

    # Convert markdown-style bold to HTML for the bubble
    import re
    html_answer = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', answer)
    html_answer = html_answer.replace("\n\n", "<br>")

    st.session_state.messages.append({
        "role": "assistant",
        "title": title,
        "content": html_answer
    })

    st.rerun()