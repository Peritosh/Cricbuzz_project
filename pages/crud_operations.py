import streamlit as st
import pandas as pd
from utils.db_connection import get_connection

st.title("⚙️ CRUD Operations")

conn = get_connection()
cursor = conn.cursor()

# TABS
tab1, tab2, tab3, tab4 = st.tabs(["➕ Create", "📖 Read", "✏️ Update", "❌ Delete"])


#CREATE
with tab1:
    st.subheader("Add Player")

    name = st.text_input("Name", key="create_name")
    country = st.text_input("Country", key="create_country")
    role = st.selectbox("Role", ["Batsman", "Bowler", "All-rounder"], key="create_role")
    game_format = st.selectbox("Format", ["ODI", "Test", "T20"], key="create_format")

    matches = st.number_input("Matches", 0, key="create_matches")
    runs = st.number_input("Runs", 0, key="create_runs")
    wickets = st.number_input("Wickets", 0, key="create_wickets")

    if st.button("Add Player"):
        if name:
            cursor.execute("""
                INSERT INTO players (name, country, role, format, matches, runs, wickets)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, country, role, game_format, matches, runs, wickets))

            conn.commit()
            st.success("Player added!")
        else:
            st.warning("Please enter player name")


#READ
with tab2:
    st.subheader("View Players")

    df = pd.read_sql("SELECT * FROM players", conn)
    st.dataframe(df, use_container_width=True)

#UPDATE
with tab3:
    st.subheader("Update Player")

    df = pd.read_sql("SELECT * FROM players", conn)

    if not df.empty:
        # Create unique display
        df["display"] = df["name"] + " (" + df["format"] + ")"

        selected_player = st.selectbox(
            "Select Player",
            df["display"],
            key="update_player"
        )

        selected_row = df[df["display"] == selected_player].iloc[0]

        new_runs = st.number_input(
            "Runs",
            value=int(selected_row["runs"]),
            key="update_runs"
        )

        new_wickets = st.number_input(
            "Wickets",
            value=int(selected_row["wickets"]),
            key="update_wickets"
        )

        new_format = st.selectbox(
            "Format",
            ["ODI", "Test", "T20"],
            index=["ODI", "Test", "T20"].index(selected_row["format"]),
            key="update_format"
        )

        if st.button("Update"):
            cursor.execute("""
                UPDATE players
                SET runs=?, wickets=?, format=?
                WHERE id=?
            """, (new_runs, new_wickets, new_format, selected_row["id"]))

            conn.commit()
            st.success("Player updated!")


#DELETE
with tab4:
    st.subheader("Delete Player")

    df = pd.read_sql("SELECT * FROM players", conn)

    if not df.empty:
        df["display"] = df["name"] + " (" + df["format"] + ")"

        selected_player = st.selectbox(
            "Select Player",
            df["display"],
            key="delete_player"
        )

        selected_row = df[df["display"] == selected_player].iloc[0]

        if st.button("Delete"):
            cursor.execute(
                "DELETE FROM players WHERE id=?",
                (selected_row["id"],)
            )
            conn.commit()
            st.success("Player deleted!")