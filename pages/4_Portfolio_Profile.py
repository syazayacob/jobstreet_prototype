import streamlit as st

st.markdown('<div class="page-title">My professional profile</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Showcase your education, skills, certifications and project experience to potential employers.</div>', unsafe_allow_html=True)

left, right = st.columns([1, 2.2])
with left:
    st.markdown("""
    <div class="panel" style="text-align:center;">
      <div style="font-size:3rem;">👩‍💻</div>
      <div style="font-size:1.15rem;font-weight:800;color:#172b4d;">Syaza Amani</div>
      <div style="color:#68778d;font-size:.85rem;">Data Science Graduate</div>
      <hr>
      <div style="font-size:.85rem;color:#52627a;">Kuching, Sarawak</div>
      <div style="font-size:.85rem;color:#52627a;">Open to opportunities</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("#### Profile completion")
    st.progress(0.85)
    st.caption("85% complete · Sample indicator")
    st.markdown("#### Core skills")
    for skill in ["Python", "SQL", "Power BI", "Tableau", "Data Analysis", "Streamlit"]:
        st.markdown(f'<span class="pill">{skill}</span>', unsafe_allow_html=True)

with right:
    st.markdown("#### About me")
    st.write(
        "A Data Science graduate with a Computer Science background and an interest in "
        "data analysis, business systems and technology-driven problem solving."
    )
    st.markdown("#### Education")
    with st.container(border=True):
        st.markdown("**Master's Degree in Data Science**")
        st.caption("Add institution and graduation year")
    with st.container(border=True):
        st.markdown("**Bachelor's Degree in Computer Science**")
        st.caption("Add institution and graduation year")

    st.markdown("#### Projects and portfolio")
    for i, project in enumerate(st.session_state.projects):
        with st.container(border=True):
            st.markdown(f"**{project['title']}**")
            st.caption(project["category"])
            st.write(project["description"])
            st.caption("Tools: " + project["tools"])
            if st.button("Remove project", key=f"remove_project_{i}"):
                st.session_state.projects.pop(i)
                st.rerun()

st.divider()
st.markdown("#### Add a project")
with st.form("add_project_form", clear_on_submit=True):
    title = st.text_input("Project title")
    category = st.selectbox("Project category", ["Academic Project", "Personal Project", "Professional Project"])
    description = st.text_area("Project description", placeholder="Describe the objective, your contribution and the outcome.")
    tools = st.text_input("Tools and technologies", placeholder="e.g. Python, SQL, Power BI")
    submitted = st.form_submit_button("Add project", type="primary")

    if submitted:
        if title.strip() and description.strip():
            st.session_state.projects.append({
                "title": title.strip(),
                "description": description.strip(),
                "tools": tools.strip() or "Not specified",
                "category": category,
            })
            st.success("Project added to this prototype session.")
            st.rerun()
        else:
            st.error("Please enter at least a project title and description.")

st.caption("Profile information is demonstration content. Changes are stored only in the current Streamlit session.")

