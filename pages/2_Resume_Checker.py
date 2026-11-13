
import streamlit as st
from pathlib import Path


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Resume Compatibility Checker",
    page_icon="📄",
    layout="wide"
)


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

    /* Main content spacing */
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

    /* Markdown lists */
    div[data-testid="stMarkdownContainer"] ul li,
    div[data-testid="stMarkdownContainer"] ul li p {{
        color: {TEXT_DARK} !important;
        font-size: 15px !important;
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
        padding: 0.55rem 1.2rem;
        font-weight: 600;
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        background-color: {DARK_BLUE};
        color: {WHITE};
        border: none;
    }}

    /* Input labels */
    .stTextInput label,
    .stSelectbox label,
    .stFileUploader label {{
        color: {TEXT_DARK} !important;
        font-weight: 600;
    }}

    /* Select box */
    div[data-baseweb="select"] > div {{
        border-radius: 8px;
        border-color: {BORDER};
    }}

    /* File uploader */
    div[data-testid="stFileUploader"] {{
        background-color: {WHITE};
        border: 1px dashed {JOBSTREET_BLUE};
        border-radius: 10px;
        padding: 15px;
    }}

    div[data-testid="stFileUploader"] section {{
        background-color: {WHITE};
    }}

    /* Alerts */
    div[data-testid="stAlert"] {{
        border-radius: 8px;
    }}

    /* General content card */
    .content-card {{
        background-color: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0, 59, 112, 0.04);
    }}

    /* Score card */
    .score-card {{
        background-color: {WHITE};
        border: 1px solid {BORDER};
        border-left: 5px solid {JOBSTREET_BLUE};
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        min-height: 190px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0 2px 8px rgba(0, 59, 112, 0.05);
    }}

    .score-label {{
        color: {TEXT_GREY};
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 12px;
    }}

    .score-number {{
        color: {JOBSTREET_BLUE};
        font-size: 48px;
        font-weight: 800;
        line-height: 1.2;
        margin: 0;
    }}

    .score-description {{
        color: {TEXT_GREY};
        font-size: 13px;
        margin-top: 10px;
    }}

    /* Feedback items */
    .feedback-item {{
        background-color: {LIGHT_BLUE};
        border-radius: 8px;
        padding: 13px 15px;
        margin-bottom: 12px;
        color: {TEXT_DARK};
        font-size: 14px;
        line-height: 1.6;
    }}

    .feedback-item strong {{
        color: {DARK_BLUE};
    }}

    /* Checklist card */
    .checklist-card {{
        background-color: {WHITE};
        border: 1px solid {BORDER};
        border-radius: 12px;
        padding: 22px;
        min-height: 190px;
    }}

    .checklist-card ul {{
        padding-left: 22px;
        margin-bottom: 0;
    }}

    .checklist-card li {{
        color: {TEXT_DARK};
        font-size: 15px;
        margin-bottom: 12px;
    }}

    /* Status labels */
    .status-good {{
        color: #218838;
        background-color: #E8F5E9;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }}

    .status-warning {{
        color: #B7791F;
        background-color: #FFF4D6;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }}

    /* Progress bar */
    div[data-testid="stProgressBar"] > div > div {{
        background-color: {JOBSTREET_BLUE};
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
        <h1 style="margin-bottom: 0;">
            Resume Compatibility Checker
        </h1>
        <p style="color: {TEXT_GREY}; margin-top: 5px;">
            Review your resume and identify areas that may need
            attention before applying for a job.
        </p>
        """,
        unsafe_allow_html=True
    )

st.divider()


# ==================================================
# INTRODUCTION
# ==================================================

st.info(
    "This is an illustrative resume review prototype. "
    "The uploaded file is not processed by a real ATS system, "
    "and the sample results are not generated from the uploaded document."
)


# ==================================================
# RESUME UPLOAD AND ROLE SELECTION
# ==================================================

st.markdown("### Upload Your Resume")

left_col, right_col = st.columns([1.2, 1])

with left_col:

    st.markdown("#### Resume Details")

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "doc", "docx"],
        help="Supported formats: PDF, DOC and DOCX."
    )

    if uploaded_file is not None:
        st.success(f"File selected: {uploaded_file.name}")
    else:
        st.caption("No resume uploaded yet.")

    target_role = st.selectbox(
        "Select your target job role",
        [
            "Business Systems Analyst",
            "Data Analyst",
            "Software Engineer",
            "Project Coordinator"
        ]
    )

    st.write("")

    show_review = st.button(
        "Show Sample Resume Review",
        use_container_width=True
    )


with right_col:

    st.markdown("#### Features Checked")

    st.markdown(
        f"""
        <div class="checklist-card">
            <ul>
                <li>Contact information is present</li>
                <li>Education and qualifications are listed</li>
                <li>Skills are relevant to the target role</li>
                <li>Project or work experience is described</li>
                <li>Resume structure is clear and readable</li>
                <li>Important sections are not missing</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# SAMPLE REVIEW RESULTS
# ==================================================

if show_review:

    st.divider()

    st.markdown("## Resume Review Results")

    st.markdown(
        f"""
        <p style="color: {TEXT_GREY};">
            Sample review for the selected role:
            <strong>{target_role}</strong>
        </p>
        """,
        unsafe_allow_html=True
    )


    # ----------------------------------------------
    # SCORE AND OVERVIEW
    # ----------------------------------------------

    score_col, overview_col = st.columns([1, 1.7])

    with score_col:
        st.markdown(
            f"""
            <div class="score-card">
                <div class="score-label">
                    Illustrative Compatibility Score
                </div>
                <div class="score-number">
                    82 / 100
                </div>
                <div class="score-description">
                    Good compatibility with the selected job role
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with overview_col:
        st.markdown(
            f"""
            <div class="content-card">
                <h3 style="margin-top: 0;">Overall Assessment</h3>
                <p style="color: {TEXT_DARK};">
                    Your sample resume demonstrates a good foundation
                    for the selected role. It includes relevant
                    qualifications, technical skills and project
                    experience.
                </p>
                <p style="color: {TEXT_DARK};">
                    A few improvements could make your resume clearer
                    and help highlight your suitability for the position.
                </p>
                <p style="margin-bottom: 0;">
                    <span class="status-good">Good Compatibility</span>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ----------------------------------------------
    # FEEDBACK AND SUGGESTIONS
    # ----------------------------------------------

    st.markdown("### Suggestions for Improvement")

    feedback_col1, feedback_col2 = st.columns(2)

    with feedback_col1:
        with st.container(border=True):
            st.markdown("#### Areas to Improve")

            st.markdown("**1. Highlight relevant skills**")
            st.write(
                "Include more role-specific technical skills "
                "that match the job requirements."
            )

            st.divider()

            st.markdown("**2. Add measurable achievements**")
            st.write(
                "Include figures or outcomes to demonstrate "
                "the impact of your projects."
            )

            st.divider()

            st.markdown("**3. Improve work experience descriptions**")
            st.write(
                "Use clear action verbs to describe your "
                "responsibilities and contributions."
            )

    with feedback_col2:
        with st.container(border=True):
            st.markdown("#### Recommended Actions")

            st.markdown("**1. Tailor your resume**")
            st.write(
                "Adjust your resume content to better match "
                "the selected job role."
            )

            st.divider()

            st.markdown("**2. Strengthen project descriptions**")
            st.write(
                "Explain the tools, technologies and results "
                "from your academic or professional projects."
            )

            st.divider()

            st.markdown("**3. Review formatting**")
            st.write(
                "Maintain consistent headings, spacing "
                "and bullet points throughout the document."
            )


    # ----------------------------------------------
    # RESUME SECTION CHECKLIST
    # ----------------------------------------------

    st.markdown("### Resume Section Checklist")

    st.markdown(
        "The following checklist illustrates the sections "
        "reviewed in this sample assessment."
    )

    checklist_items = [
        ("Contact Information", "Complete", 100, True),
        ("Education and Qualifications", "Complete", 100, True),
        ("Technical Skills", "Needs Improvement", 75, False),
        ("Project / Work Experience", "Complete", 100, True),
        ("Resume Structure", "Good", 90, True),
        ("Relevant Keywords", "Needs Improvement", 65, False)
    ]

    for item_name, status, progress, is_good in checklist_items:

        item_col1, item_col2 = st.columns([2, 1])

        with item_col1:
            st.markdown(f"**{item_name}**")

        with item_col2:

            if is_good:
                st.markdown(
                    f"""
                    <span class="status-good">
                        ✓ {status}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.markdown(
                    f"""
                    <span class="status-warning">
                        ! {status}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

        st.progress(progress / 100)


    # ----------------------------------------------
    # FINAL MESSAGE
    # ----------------------------------------------

    st.success(
        "Sample review completed! Consider applying the suggestions "
        "above to improve your resume before submitting a job application."
    )

    st.caption(
        "Note: The compatibility score and feedback are illustrative "
        "sample results for demonstration purposes only. "
        "They do not represent an actual resume analysis or ATS evaluation."
    )
