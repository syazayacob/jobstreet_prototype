
import streamlit as st
from pathlib import Path

# --------------------------------------------------
# JOBSTREET COLOUR THEME
# --------------------------------------------------

JOBSTREET_BLUE = "#0066CC"
DARK_BLUE = "#003B70"
LIGHT_BLUE = "#EAF3FC"
BACKGROUND = "#F4F7FB"
WHITE = "#FFFFFF"
TEXT_DARK = "#263746"
TEXT_GREY = "#536579"
BORDER = "#DCE5EF"
GREEN = "#28A745"
ORANGE = "#F2B544"

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {BACKGROUND};
    }}

    .block-container {{
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }}

    /* Main headings */
    .page-title {{
        color: {DARK_BLUE} !important;
        font-size: 30px;
        font-weight: 750;
        margin-bottom: 4px;
    }}

    .page-subtitle {{
        color: {TEXT_GREY} !important;
        font-size: 15px;
        margin-bottom: 25px;
    }}

    h1, h2, h3, h4 {{
        color: {DARK_BLUE} !important;
    }}

    h4 {{
        font-weight: 700 !important;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
    }}

    /* General text */
    .stMarkdown p {{
        color: {TEXT_DARK};
    }}

    /* Feature checklist text */
    div[data-testid="stMarkdownContainer"] ul li,
    div[data-testid="stMarkdownContainer"] ul li p {
        color: #263746 !important;
        font-size: 15px !important;
    }

    /* Information panels */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {WHITE};
        border-color: {BORDER} !important;
        border-radius: 10px;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: {JOBSTREET_BLUE};
        color: white !important;
        border: none;
        border-radius: 7px;
        font-weight: 600;
        min-height: 42px;
    }}

    .stButton > button:hover {{
        background-color: {DARK_BLUE};
        color: white !important;
        border: none;
    }}

    /* Input labels */
    label, .stSelectbox label, .stFileUploader label {{
        color: {DARK_BLUE} !important;
        font-weight: 600 !important;
    }}

    /* Input fields */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {{
        background-color: {WHITE};
        border-color: {BORDER};
        border-radius: 7px;
    }}

    /* File uploader */
    div[data-testid="stFileUploader"] {{
        background-color: {WHITE};
        border: 1px dashed {BORDER};
        border-radius: 9px;
        padding: 12px;
    }}

    /* Score panel */
    .score-panel {{
        background-color: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 22px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        min-height: 175px;
    }}

    .metric-label {{
        color: {TEXT_GREY};
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 8px;
    }}

    .score {{
        color: {JOBSTREET_BLUE};
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 10px;
    }}

    /* Status pills */
    .pill {{
        display: inline-block;
        padding: 6px 13px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        white-space: nowrap;
    }}

    .pill-good {{
        background-color: #E3F5E9;
        color: #187443;
    }}

    .pill-review {{
        background-color: #FFF2D8;
        color: #986000;
    }}

    .pill-missing {{
        background-color: #FCE8E8;
        color: #B42318;
    }}

    /* Progress bars */
    div[data-testid="stProgressBar"] > div {{
        background-color: #DCE5EF;
        border-radius: 10px;
    }}

    div[data-testid="stProgressBar"] > div > div {{
        background-color: {JOBSTREET_BLUE};
        border-radius: 10px;
    }}

    /* Captions */
    .stCaption {{
        color: {TEXT_GREY} !important;
    }}

    /* Alerts */
    div[data-testid="stAlert"] {{
        border-radius: 8px;
    }}

    /* Divider */
    hr {{
        border-color: {BORDER};
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HEADER WITH LOGO
# --------------------------------------------------

logo_path = Path(__file__).resolve().parents[1] / "assets" / "logo.png"

header_logo, header_title = st.columns([1, 5])

with header_logo:
    if logo_path.is_file():
        st.image(str(logo_path), width=150)
    else:
        st.markdown(
            f"""
            <div style="
                color: {JOBSTREET_BLUE};
                font-size: 25px;
                font-weight: 800;
                padding-top: 5px;">
                JobStreet
            </div>
            """,
            unsafe_allow_html=True
        )

with header_title:
    st.markdown(
        f"""
        <div style="padding-top: 5px;">
            <div style="
                color: {DARK_BLUE};
                font-size: 28px;
                font-weight: 750;">
                Resume Compatibility Checker
            </div>
            <div style="
                color: {TEXT_GREY};
                font-size: 14px;">
                Review your resume and identify areas that may need attention before applying.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --------------------------------------------------
# PROTOTYPE INFORMATION
# --------------------------------------------------

st.info(
    "Prototype note: this page demonstrates a proposed "
    "resume-review experience. It does not run a real ATS "
    "scan or analyse the contents of uploaded files."
)

# --------------------------------------------------
# RESUME UPLOAD AND FEATURE DESCRIPTION
# --------------------------------------------------

left, right = st.columns([1.15, 0.85])

with left:

    with st.container(border=True):

        st.markdown("#### Upload Your Resume")

        uploaded = st.file_uploader(
            "Choose a resume file",
            type=["pdf", "doc", "docx"]
        )

        target_role = st.selectbox(
            "Target Job Role",
            [
                "Business Systems Analyst",
                "Data Analyst",
                "Software Engineer",
                "Project Coordinator"
            ]
        )

        if uploaded:

            st.success(f"File selected: {uploaded.name}")

            st.caption(
                f"File size: {uploaded.size / 1024:.1f} KB"
            )

        else:

            st.caption(
                "No file uploaded. Explore the illustrative sample results."
            )

        analyse = st.button(
            "Show Sample Resume Review",
            type="primary",
            use_container_width=True
        )

with right:

    with st.container(border=True):

        st.markdown("#### What This Feature Checks")

        st.markdown(
            """
            - Contact information is present
            - Education and qualifications are listed
            - Skills are relevant to the target role
            - Project or work experience is described
            - Resume structure is clear and readable
            - Important sections are not missing
            """
        )

        st.markdown("---")

        st.markdown("**Supported file formats**")

        st.caption("PDF, DOC and DOCX")

# --------------------------------------------------
# SAMPLE REVIEW RESULTS
# --------------------------------------------------

if analyse or "resume_demo_result" not in st.session_state:
    st.session_state.resume_demo_result = True

if st.session_state.resume_demo_result:

    st.markdown("---")

    st.markdown("#### Sample Review Results")

    score_col, feedback_col = st.columns([1, 2])

    # ----------------------------------------------
    # COMPATIBILITY SCORE
    # ----------------------------------------------

    with score_col:

        st.markdown(
            '<div class="score-panel">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="metric-label">'
            'Illustrative Compatibility Score'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="score">82 / 100</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<span class="pill pill-good">'
            'Good Starting Point'
            '</span>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.progress(0.82)

    # ----------------------------------------------
    # FEEDBACK
    # ----------------------------------------------

    with feedback_col:

        with st.container(border=True):

            st.markdown(
                f"**Target Role:** {target_role}"
            )

            st.markdown("**Suggested Areas to Review:**")

            st.write(
                "• Add measurable outcomes to project descriptions."
            )

            st.write(
                "• Include relevant tools and technical skills."
            )

            st.write(
                "• Ensure education details and dates are complete."
            )

            st.write(
                "• Use consistent headings and formatting."
            )

    # --------------------------------------------------
    # SECTION CHECKLIST
    # --------------------------------------------------

    st.markdown("#### Section Checklist")

    checklist = [
        ("Contact Information", "Complete", 1.0, "pill-good"),
        ("Education", "Complete", 1.0, "pill-good"),
        ("Technical Skills", "Review Suggested", 0.75, "pill-review"),
        ("Projects / Experience", "Add More Detail", 0.60, "pill-review"),
        ("Formatting Consistency", "Review Suggested", 0.80, "pill-review"),
    ]

    for label, result, value, css in checklist:

        with st.container(border=True):

            x, y, z = st.columns([2, 1.5, 2])

            with x:

                st.markdown(
                    f"**{label}**"
                )

            with y:

                st.markdown(
                    f'<span class="pill {css}">{result}</span>',
                    unsafe_allow_html=True
                )

            with z:

                st.progress(value)

    # --------------------------------------------------
    # NEXT STEP
    # --------------------------------------------------

    st.success(
        "Suggested next step: review the feedback and "
        "update your resume before applying."
    )

    st.caption(
        "The score and checklist are fixed demonstration content, "
        "not results from the uploaded file."
    )
