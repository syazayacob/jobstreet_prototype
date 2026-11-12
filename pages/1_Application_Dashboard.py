
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Application Dashboard",
    page_icon="📋",
    layout="wide"
)

# --------------------------------------------------
# JOBSTREET-INSPIRED COLOUR PALETTE
# --------------------------------------------------

JOBSTREET_BLUE = "#0066CC"
DARK_BLUE = "#003B70"
LIGHT_BLUE = "#EAF3FC"
BACKGROUND = "#F5F7FA"
WHITE = "#FFFFFF"
TEXT_DARK = "#263238"
TEXT_GREY = "#64748B"
BORDER = "#E2E8F0"

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

        h1, h2, h3 {{
            color: {DARK_BLUE};
        }}

        .dashboard-header {{
            background: {WHITE};
            padding: 18px 24px;
            border-radius: 12px;
            border: 1px solid {BORDER};
            margin-bottom: 22px;
        }}

        .dashboard-subtitle {{
            color: {TEXT_GREY};
            font-size: 14px;
            margin-top: -8px;
        }}

        .metric-card {{
            background: {WHITE};
            padding: 18px;
            border-radius: 12px;
            border: 1px solid {BORDER};
            min-height: 112px;
        }}

        .metric-label {{
            color: {TEXT_GREY};
            font-size: 14px;
            font-weight: 500;
        }}

        .metric-value {{
            color: {DARK_BLUE};
            font-size: 30px;
            font-weight: 700;
            margin-top: 6px;
        }}

        .section-card {{
            background: {WHITE};
            padding: 18px;
            border-radius: 12px;
            border: 1px solid {BORDER};
            margin-bottom: 16px;
        }}

        .section-heading {{
            color: {DARK_BLUE};
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 12px;
        }}

        .status {{
            display: inline-block;
            padding: 5px 11px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }}

        .status-submitted {{
            background: #E8F1FF;
            color: #2457A6;
        }}

        .status-interview {{
            background: #FFF3D6;
            color: #986500;
        }}

        .status-rejected {{
            background: #FDECEC;
            color: #B42318;
        }}

        .status-shortlisted {{
            background: #E6F6ED;
            color: #16804A;
        }}

        div[data-testid="stMetric"] {{
            background: {WHITE};
            border: 1px solid {BORDER};
            padding: 16px;
            border-radius: 12px;
        }}

        div[data-testid="stMetricLabel"] {{
            color: {TEXT_GREY};
        }}

        div[data-testid="stMetricValue"] {{
            color: {DARK_BLUE};
        }}

        div[data-testid="stDataFrame"] {{
            border: 1px solid {BORDER};
            border-radius: 10px;
            overflow: hidden;
        }}

        .stButton > button {{
            background-color: {JOBSTREET_BLUE};
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
        }}

        .stButton > button:hover {{
            background-color: {DARK_BLUE};
            color: white;
        }}

        div[data-baseweb="select"] > div {{
            border-radius: 8px;
        }}

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

header_col1, header_col2 = st.columns([1, 5])

with header_col1:
    logo_path = Path(__file__).resolve().parents[1] / "assets" / "logo.png"

    if logo_path.exists():
        st.image(str(logo_path), width=125)
    else:
        st.markdown(
            f"<h2 style='color:{JOBSTREET_BLUE};'>JobStreet</h2>",
            unsafe_allow_html=True
        )

with header_col2:
    st.markdown(
        f"""
        <div style="padding-top: 8px;">
            <h1 style="margin-bottom: 0; color: {DARK_BLUE};">
                Application Dashboard
            </h1>
            <p class="dashboard-subtitle">
                Track and manage all your job applications in one place.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# --------------------------------------------------
# SAMPLE APPLICATION DATA
# --------------------------------------------------

if "applications" not in st.session_state:
    st.session_state.applications = pd.DataFrame([
        {
            "Company": "Sarawak Energy Berhad",
            "Position": "Data Analyst",
            "Location": "Kuching, Sarawak",
            "Date Applied": "2026-10-20",
            "Status": "Interview"
        },
        {
            "Company": "Bintulu Port Holdings",
            "Position": "Business Systems Analyst",
            "Location": "Bintulu, Sarawak",
            "Date Applied": "2026-10-25",
            "Status": "Shortlisted"
        },
        {
            "Company": "PETRONAS",
            "Position": "Software Engineer",
            "Location": "Kuala Lumpur",
            "Date Applied": "2026-10-28",
            "Status": "Submitted"
        },
        {
            "Company": "Maybank",
            "Position": "Junior Data Scientist",
            "Location": "Kuala Lumpur",
            "Date Applied": "2026-11-01",
            "Status": "Rejected"
        },
        {
            "Company": "SEB",
            "Position": "IT Support Executive",
            "Location": "Kuching, Sarawak",
            "Date Applied": "2026-11-05",
            "Status": "Submitted"
        },
        {
            "Company": "DHL",
            "Position": "Project Coordinator",
            "Location": "Kuching, Sarawak",
            "Date Applied": "2026-11-08",
            "Status": "Shortlisted"
        }
    ])

df = st.session_state.applications.copy()

# --------------------------------------------------
# SUMMARY METRICS
# --------------------------------------------------

total_applications = len(df)
submitted_count = (df["Status"] == "Submitted").sum()
shortlisted_count = (df["Status"] == "Shortlisted").sum()
interview_count = (df["Status"] == "Interview").sum()

st.markdown("### Overview")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:
    st.metric("Total Applications", total_applications)

with metric2:
    st.metric("Submitted", submitted_count)

with metric3:
    st.metric("Shortlisted", shortlisted_count)

with metric4:
    st.metric("Interviews", interview_count)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------------------------
# APPLICATION STATUS AND APPLICATION TREND CHARTS
# --------------------------------------------------

left_chart, right_chart = st.columns([1, 1.5])

# STATUS DISTRIBUTION CHART - SHORTER
with left_chart:
    st.markdown("### Application Status")

    status_data = (
        df["Status"]
        .value_counts()
        .reset_index()
    )

    status_data.columns = ["Status", "Count"]

    status_colours = {
        "Submitted": "#4A90E2",
        "Shortlisted": "#27AE60",
        "Interview": "#F2B544",
        "Rejected": "#E66A6A"
    }

    fig_status = px.pie(
        status_data,
        names="Status",
        values="Count",
        hole=0.65,
        color="Status",
        color_discrete_map=status_colours
    )

    fig_status.update_traces(
        textposition="inside",
        textinfo="percent",
        hovertemplate="%{label}: %{value}<extra></extra>"
    )

    fig_status.update_layout(
        height=280,
        margin=dict(t=15, b=15, l=10, r=10),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        paper_bgcolor=WHITE,
        plot_bgcolor=WHITE
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

# APPLICATION TREND CHART - TALLER
with right_chart:
    st.markdown("### Application Activity")

    df["Date Applied"] = pd.to_datetime(df["Date Applied"])

    trend_data = (
        df.groupby(df["Date Applied"].dt.strftime("%d %b"))
        .size()
        .reset_index(name="Applications")
    )

    trend_data.columns = ["Date", "Applications"]

    fig_trend = px.bar(
        trend_data,
        x="Date",
        y="Applications",
        text="Applications",
        color_discrete_sequence=[JOBSTREET_BLUE]
    )

    fig_trend.update_traces(
        textposition="outside",
        marker_line_width=0,
        width=0.55
    )

    fig_trend.update_layout(
        height=360,
        margin=dict(t=20, b=15, l=10, r=10),
        xaxis_title="Date Applied",
        yaxis_title="Number of Applications",
        paper_bgcolor=WHITE,
        plot_bgcolor=WHITE,
        font=dict(color=TEXT_DARK),
        yaxis=dict(
            showgrid=True,
            gridcolor="#EDF1F5",
            rangemode="tozero"
        ),
        xaxis=dict(showgrid=False)
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

st.markdown("---")

# --------------------------------------------------
# APPLICATION LIST AND FILTERS
# --------------------------------------------------

st.markdown("### My Applications")
st.caption("Search, filter and review your submitted job applications.")

filter_col1, filter_col2 = st.columns([2, 1])

with filter_col1:
    search_query = st.text_input(
        "Search by company or position",
        placeholder="e.g. Data Analyst, PETRONAS"
    )

with filter_col2:
    status_options = ["All"] + sorted(df["Status"].unique().tolist())

    selected_status = st.selectbox(
        "Filter by status",
        status_options
    )

filtered_df = df.copy()

if search_query:
    filtered_df = filtered_df[
        filtered_df["Company"].str.contains(
            search_query,
            case=False,
            na=False
        )
        |
        filtered_df["Position"].str.contains(
            search_query,
            case=False,
            na=False
        )
    ]

if selected_status != "All":
    filtered_df = filtered_df[
        filtered_df["Status"] == selected_status
    ]

display_df = filtered_df.copy()
display_df["Date Applied"] = display_df["Date Applied"].dt.strftime("%d %b %Y")

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Company": st.column_config.TextColumn("Company"),
        "Position": st.column_config.TextColumn("Job Position"),
        "Location": st.column_config.TextColumn("Location"),
        "Date Applied": st.column_config.TextColumn("Date Applied"),
        "Status": st.column_config.TextColumn("Application Status")
    }
)

st.caption(f"Showing {len(filtered_df)} of {total_applications} applications.")

# --------------------------------------------------
# APPLICATION DETAILS
# --------------------------------------------------

st.markdown("---")
st.markdown("### Application Details")

if not filtered_df.empty:

    application_options = (
        filtered_df["Company"] + " - " + filtered_df["Position"]
    ).tolist()

    selected_application = st.selectbox(
        "Select an application to view details",
        application_options
    )

    selected_index = application_options.index(selected_application)
    selected_row = filtered_df.iloc[selected_index]

    detail_col1, detail_col2 = st.columns([1.2, 1])

    with detail_col1:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-heading">Job Information</div>
                <p><b>Company:</b> {selected_row['Company']}</p>
                <p><b>Position:</b> {selected_row['Position']}</p>
                <p><b>Location:</b> {selected_row['Location']}</p>
                <p><b>Date Applied:</b> {selected_row['Date Applied'].strftime('%d %B %Y')}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with detail_col2:
        status = selected_row["Status"]

        status_class = {
            "Submitted": "status-submitted",
            "Shortlisted": "status-shortlisted",
            "Interview": "status-interview",
            "Rejected": "status-rejected"
        }.get(status, "status-submitted")

        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-heading">Application Status</div>
                <p>
                    <span class="status {status_class}">
                        {status}
                    </span>
                </p>
                <p style="color:{TEXT_GREY}; font-size:14px;">
                    Keep track of your application progress here.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

else:
    st.info("No applications match your search or filter.")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    f"""
    <div style="text-align:center; color:{TEXT_GREY}; font-size:12px;">
        Job Seeker Dashboard Concept Prototype
        <br>
        Sample data for demonstration purposes only.
    </div>
    """,
    unsafe_allow_html=True
)
