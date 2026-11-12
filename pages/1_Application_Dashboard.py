
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

    /* Section headings */
    h4 {{
        font-weight: 700 !important;
        margin-top: 20px !important;
        margin-bottom: 15px !important;
    }}

    /* Metric cards */
    div[data-testid="stMetric"] {{
        background-color: {WHITE};
        border: 1px solid {BORDER};
        border-left: 4px solid {JOBSTREET_BLUE};
        border-radius: 10px;
        padding: 17px 18px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }}

    div[data-testid="stMetricLabel"] {{
        color: {TEXT_GREY} !important;
        font-weight: 600 !important;
    }}

    div[data-testid="stMetricLabel"] p {{
        color: {TEXT_GREY} !important;
    }}

    div[data-testid="stMetricValue"] {{
        color: {DARK_BLUE} !important;
        font-weight: 750 !important;
    }}

    /* Input labels */
    label, .stSelectbox label, .stTextInput label {{
        color: {DARK_BLUE} !important;
        font-weight: 600 !important;
    }}

    /* Application cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {WHITE};
        border-color: {BORDER} !important;
        border-radius: 10px;
    }}

    /* Application title and company */
    .stMarkdown p {{
        color: {TEXT_DARK};
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

    .status-submitted {{
        background-color: #E5F0FF;
        color: #1455A0;
    }}

    .status-viewed {{
        background-color: #E8F4FC;
        color: #08769B;
    }}

    .status-shortlisted {{
        background-color: #E3F5E9;
        color: #187443;
    }}

    .status-interview {{
        background-color: #FFF2D8;
        color: #986000;
    }}

    .status-rejected {{
        background-color: #FCE8E8;
        color: #B42318;
    }}

    /* Buttons */
    .stButton > button {{
        background-color: {JOBSTREET_BLUE};
        color: white !important;
        border: none;
        border-radius: 7px;
        font-weight: 600;
    }}

    .stButton > button:hover {{
        background-color: {DARK_BLUE};
        color: white !important;
        border: none;
    }}

    /* Search and select boxes */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {{
        background-color: {WHITE};
        border-color: {BORDER};
        border-radius: 7px;
    }}

    /* Captions */
    .stCaption {{
        color: {TEXT_GREY} !important;
    }}

    /* Info messages */
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
                My Applications
            </div>
            <div style="
                color: {TEXT_GREY};
                font-size: 14px;">
                View and organise your submitted job applications in one place.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --------------------------------------------------
# APPLICATION DATA
# --------------------------------------------------

df = st.session_state.applications.copy()

# --------------------------------------------------
# SUMMARY METRICS
# --------------------------------------------------

total = len(df)

active = len(
    df[df["Status"].isin(
        ["Submitted", "Viewed", "Shortlisted", "Interview"]
    )]
)

shortlisted = len(df[df["Status"] == "Shortlisted"])
interviews = len(df[df["Status"] == "Interview"])

submitted = len(df[df["Status"] == "Submitted"])

st.markdown("#### Application Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Total Applications",
    total
)

c2.metric(
    "Submitted",
    submitted
)

c3.metric(
    "Shortlisted",
    shortlisted
)

c4.metric(
    "Interviews",
    interviews
)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# SEARCH AND FILTER
# --------------------------------------------------

left, right = st.columns([2, 1])

with left:
    search_text = st.text_input(
        "Search applications",
        placeholder="Search by job title or company"
    )

with right:
    status_filter = st.selectbox(
        "Filter by status",
        [
            "All statuses",
            "Submitted",
            "Viewed",
            "Shortlisted",
            "Interview",
            "Rejected"
        ]
    )

filtered = df.copy()

if search_text:
    filtered = filtered[
        filtered["Job title"].str.contains(
            search_text,
            case=False,
            na=False
        )
        |
        filtered["Company"].str.contains(
            search_text,
            case=False,
            na=False
        )
    ]

if status_filter != "All statuses":
    filtered = filtered[
        filtered["Status"] == status_filter
    ]

# --------------------------------------------------
# APPLICATION LIST
# --------------------------------------------------

st.markdown("#### Application List")

if filtered.empty:

    st.info(
        "No applications match your search. "
        "Try changing the search term or filter."
    )

else:

    for index, row in filtered.iterrows():

        with st.container(border=True):

            a, b, c = st.columns([3, 1.2, 1.1])

            with a:

                st.markdown(
                    f"**{row['Job title']}**"
                )

                st.caption(row["Company"])

                st.caption(
                    f"Applied: {row['Applied date']}"
                )

            with b:

                css = {
                    "Submitted": "status-submitted",
                    "Viewed": "status-viewed",
                    "Shortlisted": "status-shortlisted",
                    "Interview": "status-interview",
                    "Rejected": "status-rejected"
                }.get(
                    row["Status"],
                    "status-submitted"
                )

                st.markdown(
                    f'<span class="pill {css}">'
                    f'{row["Status"]}'
                    f'</span>',
                    unsafe_allow_html=True
                )

            with c:

                if st.button(
                    "View details",
                    key=f"details_{index}"
                ):

                    st.session_state.selected_application = row["Job title"]

# --------------------------------------------------
# APPLICATION DETAILS
# --------------------------------------------------

selected = st.session_state.get("selected_application")

if selected:

    result = df[df["Job title"] == selected]

    if not result.empty:

        row = result.iloc[0]

        st.markdown("#### Application Details")

        st.info(
            f"**{row['Job title']}** at **{row['Company']}** "
            f"— demo status: **{row['Status']}**. "
            "In a live system, status information would depend "
            "on updates supplied by the employer or platform."
        )

# --------------------------------------------------
# APPLICATION ACTIVITY OVERVIEW
# --------------------------------------------------

st.markdown("---")

st.markdown("#### Application Activity Overview")

# Count applications by status
status_counts = df["Status"].value_counts()

# Keep a consistent order for the chart
status_order = [
    "Submitted",
    "Viewed",
    "Shortlisted",
    "Interview",
    "Rejected"
]

status_counts = status_counts.reindex(
    status_order,
    fill_value=0
)

# Remove statuses with zero applications
status_counts = status_counts[status_counts > 0]

# Display bar chart
st.bar_chart(
    status_counts,
    color=JOBSTREET_BLUE,
    height=320
)

st.caption(
    "Illustrative sample data. "
    "This prototype is not connected to real employers."
)
