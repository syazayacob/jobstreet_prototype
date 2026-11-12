import streamlit as st

st.markdown('<div class="page-title">Resume Compatibility Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Review your resume and identify areas that may need attention before applying.</div>', unsafe_allow_html=True)

st.info("Prototype note: this page demonstrates a proposed resume-review experience. It does not run a real ATS scan or analyse the contents of uploaded files.")

left, right = st.columns([1.15, 0.85])
with left:
    st.markdown("#### Upload your resume")
    uploaded = st.file_uploader("Choose a resume file", type=["pdf", "doc", "docx"])
    target_role = st.selectbox("Target job role", ["Business Systems Analyst", "Data Analyst", "Software Engineer", "Project Coordinator"])
    if uploaded:
        st.success(f"File selected: {uploaded.name}")
        st.caption(f"File size: {uploaded.size / 1024:.1f} KB")
    else:
        st.caption("No file uploaded. Explore the illustrative sample results.")
    analyse = st.button("Show sample resume review", type="primary", use_container_width=True)

with right:
    st.markdown("#### What this feature checks")
    st.markdown("""
    - Contact information is present
    - Education and qualifications are listed
    - Skills are relevant to the target role
    - Project or work experience is described
    - Resume structure is clear and readable
    - Important sections are not missing
    """)

if analyse or "resume_demo_result" not in st.session_state:
    st.session_state.resume_demo_result = True

if st.session_state.resume_demo_result:
    st.divider()
    st.markdown("#### Sample review results")
    score_col, feedback_col = st.columns([1, 2])
    with score_col:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="metric-label">Illustrative compatibility score</div>', unsafe_allow_html=True)
        st.markdown('<div class="score">82 / 100</div>', unsafe_allow_html=True)
        st.progress(0.82)
        st.markdown('<span class="pill">Good starting point</span>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with feedback_col:
        st.markdown(f"**Target role:** {target_role}")
        st.markdown("**Suggested areas to review:**")
        st.write("• Add measurable outcomes to project descriptions.")
        st.write("• Include relevant tools and technical skills.")
        st.write("• Ensure education details and dates are complete.")
        st.write("• Use consistent headings and formatting.")

    st.markdown("#### Section checklist")
    checklist = [
        ("Contact information", "Complete", 1.0),
        ("Education", "Complete", 1.0),
        ("Technical skills", "Review suggested", 0.75),
        ("Projects / experience", "Add more detail", 0.60),
        ("Formatting consistency", "Review suggested", 0.80),
    ]
    for label, result, value in checklist:
        x, y, z = st.columns([2, 1.3, 2])
        x.write(label)
        y.caption(result)
        z.progress(value)

    st.success("Suggested next step: review the feedback and update your resume before applying.")
    st.caption("The score and checklist are fixed demonstration content, not results from the uploaded file.")

