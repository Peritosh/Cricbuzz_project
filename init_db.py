from utils.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

from utils.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()


#CREATE TABLES

#PLAYERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    role TEXT,
    format TEXT,
    matches INTEGER,
    runs INTEGER,
    wickets INTEGER
)
""")

#TEAMS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT
)
""")

#VENUES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    city TEXT,
    country TEXT,
    capacity INTEGER
)
""")

#MATCHES TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_desc TEXT,
    team1_id INTEGER,
    team2_id INTEGER,
    winner_id INTEGER,
    match_date TEXT,
    format TEXT,
    venue_id INTEGER
)
""")

#CLEAR OLD DATA (FOR CLEAN RESET)
cursor.execute("DELETE FROM players")
cursor.execute("DELETE FROM teams")
cursor.execute("DELETE FROM venues")
cursor.execute("DELETE FROM matches")


#INSERT PLAYERS DATA
players_data = [
    ("Virat Kohli", "India", "Batsman", "ODI", 274, 12898, 4),
    ("Virat Kohli", "India", "Batsman", "Test", 111, 8676, 0),
    ("Rohit Sharma", "India", "Batsman", "ODI", 250, 10000, 8),
    ("KL Rahul", "India", "Batsman", "T20", 75, 2800, 0),
    ("Hardik Pandya", "India", "All-rounder", "ODI", 86, 2000, 70),
    ("Ravindra Jadeja", "India", "All-rounder", "Test", 190, 2700, 220),
    ("Jasprit Bumrah", "India", "Bowler", "ODI", 89, 200, 150),
    ("Mohammed Shami", "India", "Bowler", "ODI", 90, 300, 170),

    ("Steve Smith", "Australia", "Batsman", "Test", 150, 9500, 20),
    ("David Warner", "Australia", "Batsman", "ODI", 140, 8000, 0),
    ("Glenn Maxwell", "Australia", "All-rounder", "ODI", 130, 3500, 60),
    ("Pat Cummins", "Australia", "Bowler", "Test", 85, 400, 160),
    ("Mitchell Starc", "Australia", "Bowler", "ODI", 110, 500, 220),

    ("Joe Root", "England", "Batsman", "Test", 170, 11000, 30),
    ("Ben Stokes", "England", "All-rounder", "Test", 105, 6000, 200),
    ("Jos Buttler", "England", "Wicket-keeper", "ODI", 160, 4500, 0),

    ("Kane Williamson", "New Zealand", "Batsman", "Test", 160, 9000, 20),
    ("Trent Boult", "New Zealand", "Bowler", "ODI", 95, 300, 180),

    ("Babar Azam", "Pakistan", "Batsman", "ODI", 117, 5729, 0),
    ("Shaheen Afridi", "Pakistan", "Bowler", "ODI", 60, 150, 120),

    ("Quinton de Kock", "South Africa", "Wicket-keeper", "ODI", 140, 5500, 0),
    ("Kagiso Rabada", "South Africa", "Bowler", "Test", 90, 400, 180),

    ("Shakib Al Hasan", "Bangladesh", "All-rounder", "ODI", 230, 7000, 300),
    ("Angelo Mathews", "Sri Lanka", "All-rounder", "Test", 180, 6000, 150),

    ("Chris Gayle", "West Indies", "Batsman", "ODI", 300, 10480, 20),
    ("Andre Russell", "West Indies", "All-rounder", "T20", 120, 2500, 130),

    ("Rashid Khan", "Afghanistan", "Bowler", "T20", 80, 200, 150),

    ("MS Dhoni", "India", "Wicket-keeper", "ODI", 350, 10773, 0),
    ("AB de Villiers", "South Africa", "Batsman", "ODI", 228, 9577, 0),
    ("Jacques Kallis", "South Africa", "All-rounder", "Test", 166, 13289, 292)
]

cursor.executemany("""
INSERT INTO players (name, country, role, format, matches, runs, wickets)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", players_data)

#INSERT TEAMS
teams = [
    ("India", "India"),
    ("Australia", "Australia"),
    ("England", "England"),
    ("Pakistan", "Pakistan")
]

cursor.executemany("INSERT INTO teams (name, country) VALUES (?, ?)", teams)

#INSERT VENUES
venues = [
    ("Wankhede Stadium", "Mumbai", "India", 33000),
    ("MCG", "Melbourne", "Australia", 100000),
    ("Lords", "London", "England", 30000)
]

cursor.executemany("""
INSERT INTO venues (name, city, country, capacity)
VALUES (?, ?, ?, ?)
""", venues)

#INSERT MATCHES
matches = [
    ("India vs Australia", 1, 2, 1, "2026-04-10", "ODI", 1),
    ("England vs Pakistan", 3, 4, 3, "2026-04-15", "T20", 3),
    ("Australia vs England", 2, 3, 2, "2026-03-30", "Test", 2),
    ("India vs Pakistan", 1, 4, 4, "2026-04-01", "ODI", 1)
]

cursor.executemany("""
INSERT INTO matches (match_desc, team1_id, team2_id, winner_id, match_date, format, venue_id)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", matches)

#SAVE & CLOSE
conn.commit()
conn.close()

print("✅ Database fully ready with all tables and data!")