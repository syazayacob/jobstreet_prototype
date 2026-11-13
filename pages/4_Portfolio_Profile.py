
import streamlit as st
from pathlib import Path


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
# SESSION STATE
# ==================================================

if "projects" not in st.session_state:
    st.session_state.projects = [
        {
            "title": "Extreme Rainfall Forecasting System",
            "category": "Academic Project",
            "description": (
                "Developed a forecasting application that allows users "
                "to provide weather data and view rainfall forecasting "
                "results through an interactive Streamlit interface."
            ),
            "tools": "Python, Streamlit, TCN"
        },
        {
            "title": "Web Application with Database Integration",
            "category": "Academic Project",
            "description": (
                "Developed a web application using Flask and MySQL "
                "to demonstrate application development and database "
                "integration."
            ),
            "tools": "Python, Flask, MySQL"
        }
    ]


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

    /* Containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {WHITE};
        border-color: {BORDER} !important;
        border-radius: 12px;
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

    /* Form submit button */
    .stFormSubmitButton > button {{
        background-color: {JOBSTREET_BLUE};
        color: {WHITE};
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }}

    .stFormSubmitButton > button:hover {{
        background-color: {DARK_BLUE};
        color: {WHITE};
    }}

    /* Input labels */
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {{
        color: {TEXT_DARK} !important;
        font-weight: 600;
    }}

    /* Input fields */
    div[data-baseweb="input"] > div,
    div[data-baseweb="textarea"] > div,
    div[data-baseweb="select"] > div {{
        border-radius: 8px;
        border-color: {BORDER};
    }}

    /* Profile card */
    .profile-card {{
        background-color: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 25px 18px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0, 59, 112, 0.05);
    }}

    .profile-avatar {{
        width: 85px;
        height: 85px;
        background-color: {LIGHT_BLUE};
        border-radius: 50%;
        margin: 0 auto 15px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 42px;
    }}

    .profile-name {{
        color: {DARK_BLUE};
        font-size: 21px;
        font-weight: 800;
        margin-bottom: 5px;
    }}

    .profile-role {{
        color: {TEXT_GREY};
        font-size: 14px;
        margin-bottom: 15px;
    }}

    .profile-detail {{
        color: {TEXT_GREY};
        font-size: 14px;
        margin-top: 8px;
    }}

    /* Skill tags */
    .skill-tag {{
        display: inline-block;
        background-color: {LIGHT_BLUE};
        color: {DARK_BLUE};
        border: 1px solid #C9DFF5;
        border-radius: 20px;
        padding: 6px 12px;
        margin: 4px 4px 4px 0;
        font-size: 13px;
        font-weight: 600;
    }}

    /* Profile completion */
    .completion-label {{
        color: {DARK_BLUE};
        font-size: 15px;
        font-weight: 700;
    }}

    /* Project category */
    .project-category {{
        display: inline-block;
        background-color: {LIGHT_BLUE};
        color: {JOBSTREET_BLUE};
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }}

    /* Info text */
    .muted-text {{
        color: {TEXT_GREY};
        font-size: 13px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


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
        <h1 style="margin-bottom:0;">
            My Professional Profile
        </h1>
        <p style="color:{TEXT_GREY}; margin-top:5px;">
            Showcase your education, skills, certifications and
            project experience to potential employers.
        </p>
        """,
        unsafe_allow_html=True
    )

st.divider()


# ==================================================
# PROFILE LAYOUT
# ==================================================

left, right = st.columns([1, 2.2])


# ==================================================
# LEFT COLUMN - PROFILE SUMMARY
# ==================================================

with left:

    
    
    # ----------------------------------------------
    # PROFILE INFORMATION
    # ----------------------------------------------

    with st.container(border=True):
        st.markdown(
            "<div style='text-align:center; font-size:48px;'>👩‍💻</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h3 style='text-align:center; color:#003B70;'>Syaza Amani</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center; color:#536579;'>Data Science Graduate</p>",
            unsafe_allow_html=True
        )

        st.divider()

        st.write("📍 Kuching, Sarawak")
        st.write("✓ Open to opportunities")


    # ----------------------------------------------
    # PROFILE COMPLETION
    # ----------------------------------------------

    st.markdown("#### Profile Completion")

    st.progress(0.85)

    st.caption("85% complete · Sample indicator")

    st.write("")

    # ----------------------------------------------
    # CORE SKILLS
    # ----------------------------------------------

    st.markdown("#### Core Skills")

    skills = [
        "Python",
        "SQL",
        "Power BI",
        "Tableau",
        "Looker Studio",
        "Data Analysis",
        "Streamlit"
    ]

    skill_html = ""

    for skill in skills:
        skill_html += f'<span class="skill-tag">{skill}</span>'

    st.markdown(
        skill_html,
        unsafe_allow_html=True
    )

    st.write("")

    # ----------------------------------------------
    # PROFILE STATUS
    # ----------------------------------------------

    st.markdown("#### Profile Status")

    st.success("Your profile is visible to employers.")

    st.caption(
        "Complete your profile to showcase more information "
        "about your qualifications and experience."
    )


# ==================================================
# RIGHT COLUMN - PROFESSIONAL INFORMATION
# ==================================================

with right:

    # ----------------------------------------------
    # ABOUT ME
    # ----------------------------------------------

    st.markdown("#### About Me")

    with st.container(border=True):

        st.write(
            "A Data Science graduate with a Computer Science "
            "background and an interest in data analysis, "
            "business systems and technology-driven problem solving."
        )

        st.write(
            "Experienced in academic projects involving data "
            "collection, analysis, forecasting and interactive "
            "application development. Familiar with Python, SQL, "
            "Power BI, Tableau and Looker Studio."
        )


    # ----------------------------------------------
    # EDUCATION
    # ----------------------------------------------

    st.markdown("#### Education")

    with st.container(border=True):

        st.markdown("**Master's Degree in Data Science**")

        st.caption("Institution and graduation year to be updated")

        st.divider()

        st.markdown("**Bachelor's Degree in Computer Science**")

        st.caption("Institution and graduation year to be updated")


    # ----------------------------------------------
    # EXPERIENCE
    # ----------------------------------------------

    st.markdown("#### Professional Experience")

    with st.container(border=True):

        st.markdown("**ICT Internship Programme**")

        st.caption("Sarawak Energy Berhad")

        st.write(
            "Supported in-house teams in ICT system implementation, "
            "technical issue resolution and operational monitoring."
        )

        st.write(
            "Assisted with reporting, coordinated support activities "
            "and followed up on technical matters in a timely manner."
        )


    # ----------------------------------------------
    # PROJECTS AND PORTFOLIO
    # ----------------------------------------------

    st.markdown("#### Projects and Portfolio")

    if not st.session_state.projects:

        with st.container(border=True):
            st.info(
                "No projects added yet. Use the form below "
                "to showcase your project experience."
            )

    else:

        for i, project in enumerate(st.session_state.projects):

            with st.container(border=True):

                project_col1, project_col2 = st.columns([4, 1])

                with project_col1:

                    st.markdown(f"**{project['title']}**")

                    st.markdown(
                        f"""
                        <span class="project-category">
                            {project['category']}
                        </span>
                        """,
                        unsafe_allow_html=True
                    )

                with project_col2:

                    remove_clicked = st.button(
                        "Remove",
                        key=f"remove_project_{i}"
                    )

                st.write(project["description"])

                st.caption(
                    "Tools and technologies: "
                    + project["tools"]
                )

                if remove_clicked:

                    st.session_state.projects.pop(i)

                    st.rerun()


# ==================================================
# ADD A PROJECT
# ==================================================

st.divider()

st.markdown("### Add a Project")

st.markdown(
    f"""
    <p style="color:{TEXT_GREY};">
        Add your academic, personal or professional projects
        to showcase your technical skills and experience.
    </p>
    """,
    unsafe_allow_html=True
)

with st.container(border=True):

    with st.form("add_project_form", clear_on_submit=True):

        title = st.text_input(
            "Project Title",
            placeholder="e.g. Sales Dashboard Development"
        )

        category = st.selectbox(
            "Project Category",
            [
                "Academic Project",
                "Personal Project",
                "Professional Project"
            ]
        )

        description = st.text_area(
            "Project Description",
            placeholder=(
                "Describe the project objective, your contribution "
                "and the outcome."
            ),
            height=120
        )

        tools = st.text_input(
            "Tools and Technologies",
            placeholder="e.g. Python, SQL, Power BI"
        )

        submitted = st.form_submit_button(
            "Add Project",
            type="primary",
            use_container_width=True
        )

        if submitted:

            if title.strip() and description.strip():

                st.session_state.projects.append(
                    {
                        "title": title.strip(),
                        "description": description.strip(),
                        "tools": tools.strip() or "Not specified",
                        "category": category
                    }
                )

                st.success(
                    "Project added successfully to your profile!"
                )

                st.rerun()

            else:

                st.error(
                    "Please enter at least a project title "
                    "and project description."
                )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Profile information is demonstration content. "
    "Changes are stored only in the current Streamlit session."
)
