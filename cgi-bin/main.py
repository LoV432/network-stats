import sqlite3

db = "stats.db"

# insert all data from logs.txt
def all_data(insert):
    # connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()

    #Add data to database
    c.executemany("INSERT INTO allLogs VALUES (?,?,?,?,?,?)", insert)

    #save database and close
    conn.commit()
    conn.close()

# create top domains and top username list
def sort_data(table_name, sort, search_col):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("DELETE FROM " +table_name+"")


    c.execute(""" SELECT """+sort+""", COUNT(*) as Count
    FROM allLogs
    """+search_col+"""
    GROUP BY """+sort+"""
    ORDER BY Count DESC
    """)

    items = c.fetchall()

    c.executemany("INSERT INTO "+table_name+" VALUES (?,?)", items)
    conn.commit()
    conn.close()


# Get top 5 domains of both allowed and blocked
def get_top_5(status):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM " +status+"")
    top_5 = c.fetchmany(5)
    conn.close()  
    return top_5

# Count total blocked domains
def get_total_blocked():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM Top_Blocked")
    list = c.fetchall()
    total = 0
    for hits in list:
        total = total + int(hits[1])
    conn.close()
    return total

# Get the top user for json
def get_top_user():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM Top_User")
    name = c.fetchone()
    name = name[0]
    conn.close()
    return name

# Count Total domains for json
def get_total_domain():
    # connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT rowid FROM AllLogs ORDER BY rowid DESC")
    total_domain = c.fetchone()
    total_domain = total_domain[0]
    conn.close()
    return total_domain

# Get last 10 domains accessed for json
def get_last_10_domain():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM AllLogs ORDER BY rowid DESC")
    last_10_domain = c.fetchmany(10)
    conn.close()
    return last_10_domain

