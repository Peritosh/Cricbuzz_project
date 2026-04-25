import streamlit as st
import pandas as pd
from utils.db_connection import get_connection

st.title("SQL Queries & Analytics")

conn = get_connection()

# QUERY SELECTOR

query_number = st.selectbox(
    "Select Query",
    [f"Query {i}" for i in range(1, 26)]
)


#QUERY EXECUTION FUNCTION

def run_query(query):
    try:
        df = pd.read_sql(query, conn)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error executing query: {e}")


#WORKING QUERIES

if query_number == "Query 1":
    st.subheader("Players from India")

    query = """
    SELECT name, role, format
    FROM players
    WHERE country = 'India'
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 2":
    st.subheader("Matches in last 30 days")

    query = """
    SELECT m.match_desc, t1.name AS team1, t2.name AS team2,
           v.name AS venue, v.city, m.match_date
    FROM matches m
    JOIN teams t1 ON m.team1_id = t1.team_id
    JOIN teams t2 ON m.team2_id = t2.team_id
    JOIN venues v ON m.venue_id = v.venue_id
    WHERE m.match_date >= DATE('now', '-30 day')
    ORDER BY m.match_date DESC
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 3":
    st.subheader("Top 10 ODI Run Scorers")

    query = """
    SELECT name, runs
    FROM players
    WHERE format = 'ODI'
    ORDER BY runs DESC
    LIMIT 10
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 4":
    st.subheader("Venues with capacity > 50,000")

    query = """
    SELECT name, city, country, capacity
    FROM venues
    WHERE capacity > 50000
    ORDER BY capacity DESC
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 5":
    st.subheader("Matches won per team")

    query = """
    SELECT t.name, COUNT(*) AS wins
    FROM matches m
    JOIN teams t ON m.winner_id = t.team_id
    GROUP BY t.name
    ORDER BY wins DESC
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 6":
    st.subheader("Players per role")

    query = """
    SELECT role, COUNT(*) AS total_players
    FROM players
    GROUP BY role
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 7":
    st.subheader("Highest runs per format")

    query = """
    SELECT format, MAX(runs) AS highest_runs
    FROM players
    GROUP BY format
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 9":
    st.subheader("Top All-rounders")

    query = """
    SELECT name, runs, wickets, format
    FROM players
    WHERE role = 'All-rounder'
    AND runs > 1000 AND wickets > 50
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 10":
    st.subheader("Last 20 Matches")

    query = """
   SELECT 
    m.match_desc,
    t1.name AS team1,
    t2.name AS team2,
    v.name AS venue,
    m.match_date
    FROM matches m
    JOIN teams t1 ON m.team1_id = t1.team_id
    JOIN teams t2 ON m.team2_id = t2.team_id
    JOIN venues v ON m.venue_id = v.venue_id
    ORDER BY m.match_date DESC
    LIMIT 20;
    """

    st.code(query)
    run_query(query)


elif query_number == "Query 11":
    st.subheader("Multi-format Players")

    query = """
    SELECT name, COUNT(DISTINCT format) AS formats_played
    FROM players
    GROUP BY name
    HAVING formats_played >= 2
    """

    st.code(query)
    run_query(query)



#NOT SUPPORTED QUERIES


else:
    st.subheader(query_number)

    st.code("-- SQL Query (Conceptual)")

    st.warning("""
    ❌ This query requires advanced datasets such as:

    • Ball-by-ball data  
    • Player match performance  
    • Strike rate / economy  
    • Partnerships  
    • Time-series stats  

    These are not available in the current database.

    This query can be implemented by extending the database schema.
    """)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("### 📌 Note")

st.write("""
This page demonstrates SQL analytics using available cricket data.
Some advanced queries require extended datasets and are included as conceptual implementations.
""")