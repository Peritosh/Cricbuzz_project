import streamlit as st
from utils.api_client import get_live_matches

st.set_page_config(layout="wide")

st.title("🏏 Live Matches Dashboard")

data = get_live_matches()

if not data:
    st.error("No data fetched")
else:
    type_matches = data.get("typeMatches", [])

    for match_type in type_matches:
        for series in match_type.get("seriesMatches", []):

            series_info = series.get("seriesAdWrapper", {})
            series_name = series_info.get("seriesName", "Unknown Series")

            matches = series_info.get("matches", [])

            for match in matches:
                match_info = match.get("matchInfo", {})
                match_score = match.get("matchScore", {})

                team1 = match_info.get("team1", {}).get("teamName", "Team 1")
                team2 = match_info.get("team2", {}).get("teamName", "Team 2")

                status = match_info.get("status", "N/A")

                venue = match_info.get("venueInfo", {})
                ground = venue.get("ground", "Unknown")
                city = venue.get("city", "")

                # Scores
                t1 = match_score.get("team1Score", {}).get("inngs1", {})
                t2 = match_score.get("team2Score", {}).get("inngs1", {})

                t1_score = f"{t1.get('runs','-')}/{t1.get('wickets','-')}"
                t2_score = f"{t2.get('runs','-')}/{t2.get('wickets','-')}"

                #CARD UI USING STREAMLIT (BEST WAY)
                with st.container():
                    st.markdown(f"## 🏆 {series_name}")

                    col1, col2, col3 = st.columns([3, 1, 3])

                    with col1:
                        st.markdown(f"### 🏏 {team1}")
                        st.success(f"{t1_score}")

                    with col2:
                        st.markdown("## VS")

                    with col3:
                        st.markdown(f"### 🏏 {team2}")
                        st.warning(f"{t2_score}")

                    # Match Info
                    st.caption(f"📍 {ground}, {city}")
                    st.caption(f"📢 {status}")

                    st.divider()