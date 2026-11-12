
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

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
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    f"""
    <style>
        .stApp {{
            background: {BACKGROUND};
        }}

        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }}

        /* Page headings */
        .page-title {{
            color: {DARK_BLUE} !important;
            font-size: 30px;
            font-weight: 800;
            letter-spacing: -0.8px;
            margin-bottom: 4px;
        }}

        .page-subtitle {{
            color: {TEXT_GREY} !important;
            font-size: 14px;
            margin-bottom: 20px;
        }}

        h1, h2, h3, h4 {{
            color: {DARK_BLUE} !important;
        }}

        /* Metric cards */
        div[data-testid="stMetric"] {{
            background: {WHITE};
            border: 1px solid {BORDER};
            border-left: 4px solid {JOBSTREET_BLUE};
            padding: 16px;
            border-radius: 12px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        }}

        div[data-testid="stMetricLabel"],
        div[data-testid="stMetricLabel"] p {{
            color: {TEXT_GREY} !important;
            font-weight: 600 !important;
        }}

        div[data-testid="stMetricValue"] {{
            color: {DARK_BLUE} !important;
            font-weight: 800 !important;
        }}

        /* Input labels */
        label {{
            color: {DARK_BLUE} !important;
            font-weight: 600 !important;
        }}

        /* Application cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background: {WHITE};
            border-color: {BORDER} !important;
            border-radius: 10px;
        }}

        /* Status pills */
        .pill {{
            display: inline-block;
            border-radius: 999px;
            padding: 6px 12px;
            font-size: 12px;
            font-weight: 700;
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
        div.stButton > button {{
            border-radius: 9px;
            font-weight: 600;
        }}

        div.stButton > button[kind="primary"] {{
            background: {JOBSTREET_BLUE};
            border: 1px solid {JOBSTREET_BLUE};
            color: white;
        }}

        div.stButton > button:hover {{
            border-color: {DARK_BLUE};
        }}

        /* Text fields */
        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div {{
            background: {WHITE};
            border-radius: 8px;
            border-color: {BORDER};
        }}

        /* Captions */
        .stCaption {{
            color: {TEXT_GREY} !important;
        }}

        /* Dividers */
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

logo_col, title_col = st.columns([1, 5])

with logo_col:

    if logo_path.exists():
        st.image(str(logo_path), width=130)
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
            unsafe_allow_html=True
        )

with title_col:

    st.markdown(
        """
        <div style="padding-top:5px;">
            <div class="page-title">My Applications</div>
            <div class="page-subtitle">
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

submitted = len(df[df["Status"] == "Submitted"])

shortlisted = len(df[df["Status"] == "Shortlisted"])

interviews = len(df[df["Status"] == "Interview"])

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

# Maintain a consistent status order
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

# Convert data for Plotly
chart_data = status_counts.rename_axis(
    "Status"
).reset_index(name="Applications")

# Different colours for each bar
status_colours = {
    "Submitted": "#0872CE",
    "Viewed": "#8064C2",
    "Shortlisted": "#27AE60",
    "Interview": "#F2B544",
    "Rejected": "#E05252"
}

# Create bar chart
fig = px.bar(
    chart_data,
    x="Status",
    y="Applications",
    color="Status",
    color_discrete_map=status_colours,
    text="Applications"
)

fig.update_traces(
    textposition="outside",
    marker_line_width=0
)

fig.update_layout(
    height=320,
    showlegend=False,
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(
        color=DARK_BLUE,
        family="Arial"
    ),
    xaxis_title="Application Status",
    yaxis_title="Number of Applications",
    yaxis=dict(
        showgrid=True,
        gridcolor="#E6EBF2",
        rangemode="tozero",
        dtick=1
    ),
    xaxis=dict(
        showgrid=False
    ),
    margin=dict(
        t=25,
        b=20,
        l=10,
        r=10
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "Illustrative sample data. "
    "This prototype is not connected to real employers."
)
