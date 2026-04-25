import streamlit as st

st.set_page_config(layout="wide")

#Header
st.title("🏏 Cricbuzz Live Stats Dashboard")

st.markdown("""
Welcome to the **Cricket Analytics Dashboard** built using Streamlit and Cricbuzz API.

This app provides real-time match data, player statistics, and analytics tools.
""")

#Feature section
st.markdown("## 🚀 Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px;">
        <h3>📡 Live Matches</h3>
        <p>View real-time cricket matches, scores, and match status.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px;">
        <h3>📊 Top Stats</h3>
        <p>Explore top players by runs and wickets.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background:#111827; padding:20px; border-radius:12px;">
        <h3>🗄️ SQL Analytics</h3>
        <p>Run SQL queries and analyze cricket datasets.</p>
    </div>
    """, unsafe_allow_html=True)

#How to use 
st.markdown("## 🧭 How to Use")

st.markdown("""
- Use the sidebar to navigate between pages  
- Click **Live Matches** to see ongoing games  
- Go to **Top Stats** to explore player performance  
- Use **SQL Queries** for advanced analytics  
""")


#Note
st.info("ℹ️ Note: Some statistics are overall records due to API limitations (format-wise stats not available).")

