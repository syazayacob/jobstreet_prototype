
import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Job Seeker Prototype",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"

# --------------------------------------------------
# COLOUR THEME
# --------------------------------------------------

JOBSTREET_BLUE = "#0872CE"
DARK_BLUE = "#172B4D"
TEXT_GREY = "#536579"
BACKGROUND = "#F5F7FB"
WHITE = "#FFFFFF"
BORDER = "#E6EBF2"

# --------------------------------------------------
# SHARED STYLING
# --------------------------------------------------

st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
        }}

        .stApp {{
            background: {BACKGROUND};
        }}

        [data-testid="stSidebar"] {{
            background: {WHITE};
            border-right: 1px solid {BORDER};
        }}

        /* Main header */
        .top-header {{
            background: {WHITE};
            border: 1px solid {BORDER};
            border-radius: 13px;
            padding: 12px 20px;
            margin-bottom: 22px;
            display: flex;
            align-items: center;
        }}

        .header-title {{
            color: {DARK_BLUE};
            font-size: 25px;
            font-weight: 800;
            letter-spacing: -0.7px;
            margin: 0;
        }}

        .header-subtitle {{
            color: {TEXT_GREY};
            font-size: 12px;
            margin-top: 3px;
        }}

        /* Sidebar branding */
        .brand {{
            color: {JOBSTREET_BLUE};
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: -0.7px;
            margin-bottom: 0;
        }}

        .brand-sub {{
            color: {TEXT_GREY};
            font-size: 0.72rem;
            margin-top: 0;
        }}

        /* Page headings */
        .page-title {{
            color: {DARK_BLUE} !important;
            font-size: 1.85rem;
            font-weight: 800;
            letter-spacing: -0.8px;
            margin-bottom: 0.15rem;
        }}

        .page-subtitle {{
            color: {TEXT_GREY} !important;
            margin-bottom: 1.25rem;
        }}

        /* Panels */
        .panel {{
            background: {WHITE};
            border: 1px solid {BORDER};
            border-radius: 14px;
            padding: 18px 20px;
            margin-bottom: 14px;
        }}

        /* Metrics */
        .metric-label {{
            color: {TEXT_GREY};
            font-size: 0.82rem;
            font-weight: 600;
        }}

        .score {{
            color: {JOBSTREET_BLUE};
            font-size: 1.55rem;
            font-weight: 800;
        }}

        div[data-testid="stMetric"] {{
            background: {WHITE};
            border: 1px solid {BORDER};
            padding: 14px 16px;
            border-radius: 12px;
        }}

        div[data-testid="stMetricLabel"] {{
            color: {TEXT_GREY} !important;
        }}

        div[data-testid="stMetricValue"] {{
            color: {DARK_BLUE} !important;
        }}

        /* Status pills */
        .pill {{
            display: inline-block;
            border-radius: 999px;
            padding: 4px 10px;
            font-size: 0.74rem;
            font-weight: 700;
            background: #EAF3FF;
            color: #0866B5;
        }}

        .status-submitted {{
            background: #EAF3FF;
            color: #0866B5;
        }}

        .status-viewed {{
            background: #F0EEFE;
            color: #6554C0;
        }}

        .status-shortlisted {{
            background: #E7F7EF;
            color: #16804A;
        }}

        .status-interview {{
            background: #FFF4DF;
            color: #9A6700;
        }}

        .status-rejected {{
            background: #FFF0EF;
            color: #BF3B32;
        }}

        /* Buttons */
        div.stButton > button[kind="primary"] {{
            background: {JOBSTREET_BLUE};
            border: 1px solid {JOBSTREET_BLUE};
            border-radius: 9px;
            font-weight: 650;
            color: white;
        }}

        div.stButton > button {{
            border-radius: 9px;
        }}

        /* General text visibility */
        h1, h2, h3, h4 {{
            color: {DARK_BLUE};
        }}

        label {{
            color: {DARK_BLUE} !important;
        }}

        hr {{
            border-color: {BORDER};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# SHARED SAMPLE APPLICATION DATA
# --------------------------------------------------

if "applications" not in st.session_state:

    st.session_state.applications = pd.DataFrame(
        [
            ["Data Analyst", "ABC Technology Sdn. Bhd.", "12 Nov 2026", "Shortlisted"],
            ["Business Systems Analyst", "Digital Solutions Berhad", "10 Nov 2026", "Viewed"],
            ["Junior Data Engineer", "Sarawak Digital", "08 Nov 2026", "Submitted"],
            ["IT Project Coordinator", "Borneo Services Group", "05 Nov 2026", "Interview"],
            ["Software Engineer", "Tech Innovators Sdn. Bhd.", "01 Nov 2026", "Rejected"],
            ["Data Scientist", "Borneo Analytics Sdn. Bhd.", "15 Nov 2026", "Submitted"],
            ["System Analyst", "Digital Innovation Sdn. Bhd.", "17 Nov 2026", "Submitted"],
        ],
        columns=[
            "Job title",
            "Company",
            "Applied date",
            "Status",
        ],
    )

# --------------------------------------------------
# SHARED PROJECT DATA
# --------------------------------------------------

if "projects" not in st.session_state:

    st.session_state.projects = [
        {
            "title": "Extreme Rainfall Forecasting System",
            "description": (
                "A forecasting application that presents rainfall predictions "
                "and relevant weather information through an interactive interface."
            ),
            "tools": "Python, Streamlit, TCN, Data Analysis",
            "category": "Academic Project",
        },
        {
            "title": "Flask and MySQL Web Application",
            "description": (
                "A web application developed using Flask "
                "with MySQL for data storage and retrieval."
            ),
            "tools": "Python, Flask, MySQL",
            "category": "Academic Project",
        },
    ]

# --------------------------------------------------
# SHARED TOP HEADER - VISIBLE ON EVERY PAGE
# --------------------------------------------------

logo_col, title_col = st.columns([1, 5])

with logo_col:

    if LOGO_PATH.is_file():
        st.image(str(LOGO_PATH), width=135)
    else:
        st.markdown(
            f"""
            <div style="
                color:{JOBSTREET_BLUE};
                font-size:25px;
                font-weight:800;
                padding-top:8px;">
                job seeker
            </div>
            """,
            unsafe_allow_html=True,
        )

with title_col:

    st.markdown(
        f"""
        <div style="padding-top:5px;">
            <div style="
                color:{DARK_BLUE};
                font-size:25px;
                font-weight:800;">
                Job Seeker Prototype
            </div>

            <div style="
                color:{TEXT_GREY};
                font-size:12px;">
                BUSINESS SYSTEMS ANALYST ASSESSMENT
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# --------------------------------------------------
# SHARED SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<p class="brand">job seeker</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="brand-sub">BUSINESS SYSTEMS ANALYST PROTOTYPE</p>',
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("**Demo Account**")

    st.write("Syaza Amani")

    st.caption("Job seeker · Sample profile")

    st.divider()

    st.caption(
        "Concept prototype only. "
        "Sample information is used for demonstration."
    )

# --------------------------------------------------
# MULTIPAGE NAVIGATION
# --------------------------------------------------

pages = [
    st.Page(
        "pages/1_Application_Dashboard.py",
        title="Application Dashboard",
        icon="📋",
        default=True,
    ),

    st.Page(
        "pages/2_Resume_Checker.py",
        title="Resume Checker",
        icon="📄",
    ),

    st.Page(
        "pages/3_Job_Matching.py",
        title="Job Matching",
        icon="🎯",
    ),

    st.Page(
        "pages/4_Portfolio_Profile.py",
        title="Portfolio Profile",
        icon="👤",
    ),
]

navigation = st.navigation(pages)

# Display selected page
navigation.run()
