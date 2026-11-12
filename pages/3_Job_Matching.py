import streamlit as st

jobs = [
    {
        "title": "Business Systems Analyst",
        "company": "Digital Solutions Berhad",
        "location": "Kuching, Sarawak",
        "salary": "RM 3,500 – RM 4,500",
        "type": "Full-time",
        "skills": ["SQL", "Requirements Analysis", "Documentation", "Communication", "Process Mapping"],
        "description": "Work with stakeholders to understand business processes, document requirements and support system improvements.",
    },
    {
        "title": "Data Analyst",
        "company": "ABC Technology Sdn. Bhd.",
        "location": "Kuching, Sarawak",
        "salary": "RM 3,000 – RM 4,000",
        "type": "Full-time",
        "skills": ["Python", "SQL", "Power BI", "Excel", "Data Analysis"],
        "description": "Analyse datasets, prepare reports and dashboards, and communicate insights to business teams.",
    },
    {
        "title": "Junior Data Engineer",
        "company": "Sarawak Digital",
        "location": "Hybrid · Sarawak",
        "salary": "RM 3,200 – RM 4,200",
        "type": "Full-time",
        "skills": ["Python", "SQL", "ETL", "Data Management", "Problem Solving"],
        "description": "Assist with data pipelines, data quality checks and data integration activities.",
    },
    {
        "title": "IT Project Coordinator",
        "company": "Borneo Services Group",
        "location": "Kuching, Sarawak",
        "salary": "RM 2,800 – RM 3,600",
        "type": "Contract",
        "skills": ["Communication", "Documentation", "Coordination", "Excel", "Problem Solving"],
        "description": "Coordinate project activities, maintain documentation and follow up on project deliverables.",
    },
]

st.markdown('<div class="page-title">Jobs matched to your profile</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Explore job opportunities and understand why each role may suit your skills.</div>', unsafe_allow_html=True)

selected_skills = st.multiselect(
    "Your skills",
    ["Python", "SQL", "Power BI", "Tableau", "Data Analysis", "Requirements Analysis",
     "Documentation", "Communication", "Process Mapping", "Excel", "ETL",
     "Problem Solving", "Coordination", "Data Management"],
    default=["Python", "SQL", "Power BI", "Data Analysis", "Communication"],
)
location_filter = st.selectbox("Preferred location", ["All locations", "Kuching, Sarawak", "Sarawak", "Hybrid"])

st.divider()
st.markdown("#### Recommended opportunities")

for index, job in enumerate(jobs):
    matched = [skill for skill in job["skills"] if skill in selected_skills]
    missing = [skill for skill in job["skills"] if skill not in selected_skills]
    score = round(len(matched) / len(job["skills"]) * 100) if job["skills"] else 0

    location_ok = (
        location_filter == "All locations"
        or (location_filter == "Sarawak" and "Sarawak" in job["location"])
        or (location_filter == "Kuching, Sarawak" and "Kuching" in job["location"])
        or (location_filter == "Hybrid" and "Hybrid" in job["location"])
    )
    if not location_ok:
        continue

    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{job['title']}**")
            st.caption(f"{job['company']} · {job['location']}")
            st.caption(f"{job['salary']} · {job['type']}")
        with col2:
            st.markdown(f'<div class="score">{score}%</div>', unsafe_allow_html=True)
            st.caption("Skills match · demo")

        st.write(job["description"])
        st.markdown("**Matching skills**")
        if matched:
            st.success(" · ".join(matched))
        else:
            st.caption("No matching skills selected yet.")
        if missing:
            st.markdown("**Skills you may want to develop**")
            st.warning(" · ".join(missing))

        with st.expander("Why am I seeing this job?"):
            st.write(
                f"This illustrative match is based on the skills selected above. "
                f"{len(matched)} of {len(job['skills'])} listed skills match your selections. "
                "A real recommendation system could also consider experience, qualifications, "
                "location preferences and job-search activity."
            )
        if st.button("Save job", key=f"save_job_{index}"):
            saved = st.session_state.get("saved_jobs", [])
            if job["title"] not in saved:
                saved.append(job["title"])
                st.session_state.saved_jobs = saved
            st.toast(f"{job['title']} saved to your demo list")

saved_jobs = st.session_state.get("saved_jobs", [])
if saved_jobs:
    st.divider()
    st.markdown("**Saved jobs in this session**")
    st.write(" · ".join(saved_jobs))

st.caption("Match percentages are illustrative calculations based only on selected skills, not real JobStreet ranking.")

