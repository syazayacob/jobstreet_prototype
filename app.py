import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Job Seeker Prototype",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Shared styling for all pages
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
      html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
      .stApp { background: #f5f7fb; }
      [data-testid="stSidebar"] { background: #ffffff; border-right: 1px solid #e7edf5; }
      .brand { color:#0872ce; font-size:1.45rem; font-weight:800; letter-spacing:-.7px; margin-bottom:0; }
      .brand-sub { color:#718096; font-size:.75rem; margin-top:0; }
      .page-title { color:#172b4d; font-size:1.85rem; font-weight:800; letter-spacing:-.8px; margin-bottom:.15rem; }
      .page-subtitle { color:#68778d; margin-bottom:1.25rem; }
      .panel { background:#fff; border:1px solid #e6ebf2; border-radius:14px; padding:18px 20px; margin-bottom:14px; }
      .metric-label { color:#68778d; font-size:.82rem; font-weight:600; }
      .score { color:#0872ce; font-size:1.55rem; font-weight:800; }
      .pill { display:inline-block; border-radius:999px; padding:4px 10px; font-size:.74rem; font-weight:700; background:#eaf3ff; color:#0866b5; }
      .status-submitted { background:#eaf3ff; color:#0866b5; }
      .status-viewed { background:#f0eefe; color:#6554c0; }
      .status-shortlisted { background:#e7f7ef; color:#16804a; }
      .status-interview { background:#fff4df; color:#9a6700; }
      .status-rejected { background:#fff0ef; color:#bf3b32; }
      div.stButton > button[kind="primary"] { background:#0872ce; border:1px solid #0872ce; border-radius:9px; font-weight:650; }
      div.stButton > button { border-radius:9px; }
      div[data-testid="stMetric"] { background:#fff; border:1px solid #e6ebf2; padding:14px 16px; border-radius:12px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Shared demo data (stored in session state while the app is open)
if "applications" not in st.session_state:
    st.session_state.applications = pd.DataFrame(
        [
            ["Data Analyst", "ABC Technology Sdn. Bhd.", "12 Nov 2026", "Shortlisted"],
            ["Business Systems Analyst", "Digital Solutions Berhad", "10 Nov 2026", "Viewed"],
            ["Junior Data Engineer", "Sarawak Digital", "08 Nov 2026", "Submitted"],
            ["IT Project Coordinator", "Borneo Services Group", "05 Nov 2026", "Interview"],
            ["Software Engineer", "Tech Innovators Sdn. Bhd.", "01 Nov 2026", "Rejected"],
        ],
        columns=["Job title", "Company", "Applied date", "Status"],
    )

if "projects" not in st.session_state:
    st.session_state.projects = [
        {
            "title": "Extreme Rainfall Forecasting System",
            "description": "A forecasting application that presents rainfall predictions and relevant weather information through an interactive interface.",
            "tools": "Python, Streamlit, TCN, Data Analysis",
            "category": "Academic Project",
        },
        {
            "title": "Flask and MySQL Web Application",
            "description": "A web application developed using Flask with MySQL for data storage and retrieval.",
            "tools": "Python, Flask, MySQL",
            "category": "Academic Project",
        },
    ]

# Shared sidebar branding. Streamlit automatically discovers pages in /pages.
with st.sidebar:
    st.markdown('<p class="brand">job seeker</p>', unsafe_allow_html=True)
    st.markdown('<p class="brand-sub">BUSINESS SYSTEMS ANALYST PROTOTYPE</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown("**Demo account**")
    st.write("Syaza Amani")
    st.caption("Job seeker · Sample profile")
    st.divider()
    st.caption("Concept prototype only. Sample information is used for demonstration.")

st.markdown(
    """
    <div class="panel">
      <h3 style="color:#172b4d;margin:0 0 8px 0;">Welcome to the Job Seeker Prototype</h3>
      <p style="color:#68778d;margin:0;">
        Use the navigation menu to explore four proposed JobStreet-inspired enhancements:
        application tracking, resume review, explainable job matching, and a project portfolio.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)
st.info("Select a page from the sidebar to open a mockup.")
st.caption("This is an independent concept prototype, not an official JobStreet product.")

