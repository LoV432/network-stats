import matplotlib.pyplot as plt
import datetime
import sqlite3
import main
count = 0
names = []
values = []
values_dict = {}

# Get all times
time = datetime.datetime.now()
date = time.strftime("%Y-%b-%d")
current_time = time.strftime("%H:%M:%S")


# Connect to DB
conn = sqlite3.connect(main.db)
c = conn.cursor()


for x in range(12):

    #Get the date and hour
    hour = current_time.split(":")[0] +"%"

    #Use that day and hour to search the DB
    c.execute("""SELECT * FROM allLogs
    WHERE Date = ? AND Time LIKE ?
    ORDER BY rowid DESC""",(date, hour))

    #Once searched use loop to count all entry
    list = c.fetchall()
    for x in list:
        #print(x)
        count += 1
    
    #add it to values_dict
    hour = hour.replace("%", "")
    hour = hour + ":00"
    values_dict[hour] = count
    count = 0

    #Remove 1 hour and repeat
    time = time - datetime.timedelta(hours=1)
    current_time = time.strftime("%H:%M:%S")
    date = time.strftime("%Y-%b-%d")

for x, y in values_dict.items():
    names.append(x)
    values.append(y)

plt.figure(figsize=(10, 5))
COLOR = 'white'
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR
plt.rcParams['axes.edgecolor'] = COLOR
plt.bar(names[::-1], values[::-1])
plt.savefig("img/img", dpi=150, transparent=True)