import sqlite3

conn = sqlite3.connect("stats.db")

c = conn.cursor()

c.execute(""" CREATE TABLE allLogs (
    Date text,
    Day text,
    Time text,
    Status text,
    Domain text,
    User text
    
)""")
c.execute("CREATE TABLE Top_Allowed (Domain text, Hits text)")
c.execute("CREATE TABLE Top_Blocked (Domain text, Hits text)")
c.execute("CREATE TABLE Top_User (Name text, Hits text)")