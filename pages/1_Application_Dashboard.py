import streamlit as st

st.markdown('<div class="page-title">My Applications</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">View and organise your submitted job applications in one place.</div>', unsafe_allow_html=True)

df = st.session_state.applications.copy()
total = len(df)
active = len(df[df["Status"].isin(["Submitted", "Viewed", "Shortlisted", "Interview"])])
shortlisted = len(df[df["Status"] == "Shortlisted"])
interviews = len(df[df["Status"] == "Interview"])

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total applications", total)
c2.metric("Active applications", active)
c3.metric("Shortlisted", shortlisted)
c4.metric("Interviews", interviews)

left, right = st.columns([2, 1])
with left:
    search_text = st.text_input("Search applications", placeholder="Search by job title or company")
with right:
    status_filter = st.selectbox("Filter by status", ["All statuses", "Submitted", "Viewed", "Shortlisted", "Interview", "Rejected"])

filtered = df.copy()
if search_text:
    filtered = filtered[
        filtered["Job title"].str.contains(search_text, case=False, na=False)
        | filtered["Company"].str.contains(search_text, case=False, na=False)
    ]
if status_filter != "All statuses":
    filtered = filtered[filtered["Status"] == status_filter]

st.markdown("#### Application list")
if filtered.empty:
    st.info("No applications match your search. Try changing the search term or filter.")
else:
    for _, row in filtered.iterrows():
        with st.container(border=True):
            a, b, c = st.columns([3, 1.2, 1.1])
            with a:
                st.markdown(f"**{row['Job title']}**")
                st.caption(row["Company"])
                st.caption(f"Applied: {row['Applied date']}")
            with b:
                css = {
                    "Submitted":"status-submitted", "Viewed":"status-viewed",
                    "Shortlisted":"status-shortlisted", "Interview":"status-interview",
                    "Rejected":"status-rejected"
                }.get(row["Status"], "status-submitted")
                st.markdown(f'<span class="pill {css}">{row["Status"]}</span>', unsafe_allow_html=True)
            with c:
                if st.button("View details", key=f"details_{row['Job title']}"):
                    st.session_state.selected_application = row["Job title"]

selected = st.session_state.get("selected_application")
if selected:
    result = df[df["Job title"] == selected]
    if not result.empty:
        row = result.iloc[0]
        st.markdown("#### Application details")
        st.info(f"**{row['Job title']}** at **{row['Company']}** — demo status: **{row['Status']}**. In a live system, status information would depend on updates supplied by the employer or platform.")

st.markdown("#### Application activity overview")
st.bar_chart(df["Status"].value_counts())
st.caption("Illustrative sample data. This prototype is not connected to real employers.")
