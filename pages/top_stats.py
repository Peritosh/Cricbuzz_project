import streamlit as st
import pandas as pd
from utils.api_client import get_top_stats

st.set_page_config(layout="wide", page_title="Top Stats")

st.title("🏏 Top Cricket Stats")

#DROPDOWN
option_map = {
    "Most Runs": "mostRuns",
    "Most Wickets": "mostWickets"
}

selected_option = st.selectbox("Select Category", list(option_map.keys()))

#FETCH DATA
data = get_top_stats(option_map[selected_option])

if not data:
    st.error("Failed to fetch data")
    st.stop()

players = data.get("values", [])


#SAFE NUMBER
def safe(v):
    try:
        return float(v)
    except:
        return v


#PROCESS DATA
rows = []

for i, p in enumerate(players[:10]):
    v = p.get("values", [])

    if len(v) >= 5:
        row = {
            "Rank": i + 1,
            "Player": v[1],
            "Matches": safe(v[2]),
        }

        #DIFFERENT LOGIC BASED ON TYPE
        if selected_option == "Most Runs":
            row["Runs"] = safe(v[4])

        elif selected_option == "Most Wickets":
            row["Wickets"] = safe(v[4])

        rows.append(row)

df = pd.DataFrame(rows)

if df.empty:
    st.warning("No data found")
    st.stop()


#TOP PLAYER
top = df.iloc[0]

st.markdown("## 🏆 Top Performer")

col1, col2, col3 = st.columns(3)

col1.metric("Player", top["Player"])
col2.metric("Matches", top["Matches"])

if selected_option == "Most Runs":
    col3.metric("Runs", top["Runs"])
else:
    col3.metric("Wickets", top["Wickets"])


#CHART
st.markdown("## 📈 Chart")

if selected_option == "Most Runs":
    st.bar_chart(df.set_index("Player")["Runs"])
else:
    st.bar_chart(df.set_index("Player")["Wickets"])


#TABLE
st.markdown("## 📋 Table")
st.dataframe(df, use_container_width=True)


#PLAYER CARDS
st.markdown("## 🔥 Top Players")

for _, row in df.iterrows():

    stat_value = row.get("Runs") if "Runs" in row else row.get("Wickets")
    stat_name = "Runs" if "Runs" in row else "Wickets"

    st.markdown(f"""
    <div style="
        background:#111827;
        padding:15px;
        border-radius:10px;
        margin-bottom:10px;">
        <h4>🏏 {row['Player']} (#{int(row['Rank'])})</h4>
        <p>
        {stat_name}: <b>{stat_value}</b> |
        Matches: <b>{row['Matches']}</b>
        </p>
    </div>
    """, unsafe_allow_html=True)