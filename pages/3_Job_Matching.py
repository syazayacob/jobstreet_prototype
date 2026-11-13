
import streamlit as st
from pathlib import Path


# ==================================================
# JOB DATA
# ==================================================

jobs = [
    {
        "title": "Business Systems Analyst",
        "company": "Digital Solutions Berhad",
        "location": "Kuching, Sarawak",
        "salary": "RM 3,500 – RM 4,500",
        "type": "Full-time",
        "skills": [
            "SQL",
            "Requirements Analysis",
            "Documentation",
            "Communication",
            "Process Mapping"
        ],
        "description": (
            "Work with stakeholders to understand business processes, "
            "document requirements and support system improvements."
        ),
    },
    {
        "title": "Data Analyst",
        "company": "ABC Technology Sdn. Bhd.",
        "location": "Kuching, Sarawak",
        "salary": "RM 3,000 – RM 4,000",
        "type": "Full-time",
        "skills": [
            "Python",
            "SQL",
            "Power BI",
            "Excel",
            "Data Analysis"
        ],
        "description": (
            "Analyse datasets, prepare reports and dashboards, "
            "and communicate insights to business teams."
        ),
    },
    {
        "title": "Junior Data Engineer",
        "company": "Sarawak Digital",
        "location": "Hybrid · Sarawak",
        "salary": "RM 3,200 – RM 4,200",
        "type": "Full-time",
        "skills": [
            "Python",
            "SQL",
            "ETL",
            "Data Management",
            "Problem Solving"
        ],
        "description": (
            "Assist with data pipelines, data quality checks "
            "and data integration activities."
        ),
    },
    {
        "title": "IT Project Coordinator",
        "company": "Borneo Services Group",
        "location": "Kuching, Sarawak",
        "salary": "RM 2,800 – RM 3,600",
        "type": "Contract",
        "skills": [
            "Communication",
            "Documentation",
            "Coordination",
            "Excel",
            "Problem Solving"
        ],
        "description": (
            "Coordinate project activities, maintain documentation "
            "and follow up on project deliverables."
        ),
    },
]


# ==================================================
# JOBSTREET COLOUR THEME
# ==================================================

JOBSTREET_BLUE = "#0066CC"
DARK_BLUE = "#003B70"
LIGHT_BLUE = "#EAF3FC"
BACKGROUND = "#F4F7FB"
WHITE = "#FFFFFF"
TEXT_DARK = "#263746"
TEXT_GREY = "#536579"
BORDER = "#DCE5EF"


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    f"""
    <style>

    /* Main background */
    .stApp {{
        background-color: {BACKGROUND};
    }}

    /* Main content */
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }}

    /* General text */
    .stMarkdown p {{
        color: {TEXT_DARK};
        font-size: 15px;
    }}

    /* Page title */
    h1 {{
        color: {DARK_BLUE} !important;
        font-size: 30px !important;
        font-weight: 700 !important;
    }}

    /* Section headings */
    h2, h3, h4 {{
        color: {DARK_BLUE} !important;
        font-weight: 700 !important;
    }}

    /* Captions */
    .stCaption {{
        color: {TEXT_GREY} !important;
    }}

    /* Divider */
    hr {{
        border: none;
        border-top: 1px solid {BORDER};
        margin-top: 1.2rem;
        margin-bottom: 1.2rem;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: {JOBSTREET_BLUE};
        color: {WHITE};
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        background-color: {DARK_BLUE};
        color: {WHITE};
        border: none;
    }}

    /* Input labels */
    .stMultiSelect label,
    .stSelectbox label {{
        color: {TEXT_DARK} !important;
        font-weight: 600;
    }}

    /* Select and multiselect fields */
    div[data-baseweb="select"] > div {{
        border-radius: 8px;
        border-color: {BORDER};
        background-color: {WHITE};
    }}

    /* Job card */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {WHITE};
        border-color: {BORDER};
        border-radius: 12px;
    }}

    /* Metric styling */
    div[data-testid="stMetric"] {{
        background-color: {LIGHT_BLUE};
        border: 1px solid {BORDER};
        border-radius: 10px;
        padding: 12px 15px;
    }}

    div[data-testid="stMetricLabel"] {{
        color: {TEXT_GREY};
        font-weight: 600;
    }}

    div[data-testid="stMetricValue"] {{
        color: {JOBSTREET_BLUE};
        font-weight: 800;
    }}

    /* Expanders */
    div[data-testid="stExpander"] {{
        border: 1px solid {BORDER};
        border-radius: 8px;
        background-color: {WHITE};
    }}

    /* Alerts */
    div[data-testid="stAlert"] {{
        border-radius: 8px;
    }}

    /* Progress bars */
    div[data-testid="stProgressBar"] > div > div {{
        background-color: {JOBSTREET_BLUE};
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SESSION STATE
# ==================================================

if "saved_jobs" not in st.session_state:
    st.session_state.saved_jobs = []


# ==================================================
# HEADER
# ==================================================

logo_path = Path(__file__).resolve().parents[1] / "assets" / "logo.png"

header_col1, header_col2 = st.columns([1, 5])

with header_col1:
    if logo_path.exists():
        st.image(str(logo_path), width=800)

with header_col2:
    st.markdown(
        f"""
        <h1 style="margin-bottom: 0;">
            Job Matching
        </h1>

        <p style="color: {TEXT_GREY}; margin-top: 5px;">
            Explore job opportunities matched to your skills
            and preferred location.
        </p>
        """,
        unsafe_allow_html=True
    )

st.divider()


# ==================================================
# PROFILE SKILLS AND FILTERS
# ==================================================

st.markdown("### Your Job Preferences")

st.write(
    "Select your skills and preferred location to discover "
    "job opportunities that may match your profile."
)

available_skills = [
    "Python",
    "SQL",
    "Power BI",
    "Tableau",
    "Data Analysis",
    "Requirements Analysis",
    "Documentation",
    "Communication",
    "Process Mapping",
    "Excel",
    "ETL",
    "Problem Solving",
    "Coordination",
    "Data Management"
]

filter_col1, filter_col2 = st.columns([2, 1])

with filter_col1:
    selected_skills = st.multiselect(
        "Your skills",
        available_skills,
        default=[
            "Python",
            "SQL",
            "Power BI",
            "Data Analysis",
            "Communication"
        ],
        placeholder="Select your skills"
    )

with filter_col2:
    location_filter = st.selectbox(
        "Preferred location",
        [
            "All locations",
            "Kuching, Sarawak",
            "Sarawak",
            "Hybrid"
        ]
    )


# ==================================================
# FILTER JOBS
# ==================================================

filtered_jobs = []

for job in jobs:

    location_ok = (
        location_filter == "All locations"
        or (
            location_filter == "Sarawak"
            and "Sarawak" in job["location"]
        )
        or (
            location_filter == "Kuching, Sarawak"
            and "Kuching" in job["location"]
        )
        or (
            location_filter == "Hybrid"
            and "Hybrid" in job["location"]
        )
    )

    if location_ok:
        filtered_jobs.append(job)


# ==================================================
# SUMMARY METRICS
# ==================================================

st.divider()

total_jobs = len(filtered_jobs)
total_saved = len(st.session_state.saved_jobs)

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(
        "Available Opportunities",
        total_jobs
    )

with metric_col2:
    st.metric(
        "Selected Skills",
        len(selected_skills)
    )

with metric_col3:
    st.metric(
        "Saved Jobs",
        total_saved
    )


# ==================================================
# RECOMMENDED JOB OPPORTUNITIES
# ==================================================

st.markdown("### Recommended Opportunities")

st.caption(
    "Explore job details, compare your skills and save opportunities "
    "that interest you."
)


if not filtered_jobs:

    st.info(
        "No job opportunities found for the selected location. "
        "Try selecting another location."
    )

else:

    for index, job in enumerate(filtered_jobs):

        matched = [
            skill for skill in job["skills"]
            if skill in selected_skills
        ]

        missing = [
            skill for skill in job["skills"]
            if skill not in selected_skills
        ]

        score = (
            round(len(matched) / len(job["skills"]) * 100)
            if job["skills"]
            else 0
        )

        is_saved = job["title"] in st.session_state.saved_jobs

        with st.container(border=True):

            # --------------------------------------
            # JOB TITLE AND MATCH SCORE
            # --------------------------------------

            job_col1, job_col2 = st.columns([3, 1])

            with job_col1:

                st.markdown(f"### {job['title']}")

                st.caption(
                    f"{job['company']}  ·  {job['location']}"
                )

                st.markdown(
                    f"**{job['salary']}**  ·  {job['type']}"
                )

            with job_col2:

                st.metric(
                    "Skills Match",
                    f"{score}%"
                )

                st.caption("Illustrative match")


            # --------------------------------------
            # JOB DESCRIPTION
            # --------------------------------------

            st.write(job["description"])

            st.divider()


            # --------------------------------------
            # SKILL MATCHING
            # --------------------------------------

            match_col1, match_col2 = st.columns(2)

            with match_col1:

                st.markdown("**Matching Skills**")

                if matched:
                    st.success(" · ".join(matched))
                else:
                    st.caption(
                        "No matching skills selected yet."
                    )

            with match_col2:

                st.markdown("**Skills to Develop**")

                if missing:
                    st.warning(" · ".join(missing))
                else:
                    st.success(
                        "All listed skills match your selections."
                    )


            # --------------------------------------
            # MATCH EXPLANATION
            # --------------------------------------

            with st.expander("Why am I seeing this job?"):

                st.write(
                    f"This illustrative match is based on the skills "
                    f"selected above. {len(matched)} of "
                    f"{len(job['skills'])} listed skills match "
                    f"your selections."
                )

                st.write(
                    "A real recommendation system could also consider "
                    "work experience, qualifications, location preferences "
                    "and job-search activity."
                )


            # --------------------------------------
            # SAVE JOB BUTTON
            # --------------------------------------

            button_col1, button_col2 = st.columns([1, 3])

            with button_col1:

                if not is_saved:

                    if st.button(
                        "☆ Save Job",
                        key=f"save_job_{index}",
                        use_container_width=True
                    ):

                        st.session_state.saved_jobs.append(
                            job["title"]
                        )

                        st.toast(
                            f"{job['title']} saved successfully!"
                        )

                        st.rerun()

                else:

                    st.button(
                        "✓ Saved",
                        key=f"saved_job_{index}",
                        disabled=True,
                        use_container_width=True
                    )


# ==================================================
# SAVED JOBS
# ==================================================

if st.session_state.saved_jobs:

    st.divider()

    st.markdown("### Saved Jobs")

    st.write(
        "Your saved opportunities are kept during this session."
    )

    for saved_title in st.session_state.saved_jobs:

        saved_job = next(
            (
                job for job in jobs
                if job["title"] == saved_title
            ),
            None
        )

        if saved_job:

            with st.container(border=True):

                saved_col1, saved_col2 = st.columns([4, 1])

                with saved_col1:

                    st.markdown(f"**{saved_job['title']}**")

                    st.caption(
                        f"{saved_job['company']} · "
                        f"{saved_job['location']}"
                    )

                with saved_col2:

                    st.caption(saved_job["salary"])


# ==================================================
# FOOTER NOTE
# ==================================================

st.divider()

st.caption(
    "Note: Match percentages are illustrative calculations based "
    "only on the selected skills. They do not represent actual "
    "JobStreet recommendation rankings or recruitment decisions."
)
