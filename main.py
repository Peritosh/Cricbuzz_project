import streamlit as st

st.set_page_config(
    page_title="Cricbuzz Dashboard",
    page_icon="🏏",
    layout="wide"
)

#HEADER
st.title("🏏 Cricbuzz Analytics Dashboard")

st.markdown("""
Welcome to the **Cricket Analytics Dashboard** built using **Streamlit + Cricbuzz API**.

Explore live matches, player stats, SQL analytics, and database operations.
""")

st.info("👈 Use the sidebar or buttons below to navigate")

#FEATURE CARDS
st.markdown("## 📌 Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px;">
        <h3>📡 Live Matches</h3>
        <p>View live scores, match status, and detailed scorecards.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px; margin-top:10px;">
        <h3>📊 Top Stats</h3>
        <p>Explore top players by runs, wickets, and records.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px;">
        <h3>🗄️ SQL Analytics</h3>
        <p>Run advanced SQL queries on cricket datasets.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px; margin-top:10px;">
        <h3>⚙️ CRUD Operations</h3>
        <p>Perform create, read, update, delete operations.</p>
    </div>
    """, unsafe_allow_html=True)


#NAVIGATION BUTTONS
st.markdown("## 🚀 Quick Navigation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📡 Live Matches"):
        st.switch_page("pages/live_matches.py")

with col2:
    if st.button("📊 Top Stats"):
        st.switch_page("pages/top_stats.py")

with col3:
    if st.button("⚙️ CRUD"):
        st.switch_page("pages/crud_operations.py")

with col4:
    if st.button("🗄️ SQL Queries"):
        st.switch_page("pages/sql_queries.py")

#Note
st.warning("⚠️ Some stats are overall records due to API limitations (no format-wise filtering).")

