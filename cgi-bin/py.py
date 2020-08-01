import sys
import sqlite3
import main
import json
import datetime

try:
    conn = sqlite3.connect(main.db)
    c = conn.cursor()
    c.execute("SELECT * FROM Top_Blocked")
    conn.close()
except:
    main.create_database()
    print("Database Created")

#Get Year for sorting data later
time = datetime.datetime.now()
year = time.strftime("%Y")

# Convert IP to Name
x = ""
def name_convert():
    global x
    x = x.replace("IP", "NAME")
    x = x.replace("IP", "NAME")
    x = x.replace("IP", "NAME")
    x = x.replace("IP", "NAME")
    x = x.replace("IP", "NAME")

insert = []

# read the logs.txt file and clear file
l = open('logs.txt', 'r')
allLogs = l.read()
open('logs.txt', 'w').close()

# split the whole text by <30> <29>
allLogs = allLogs.replace("<29>", "<30>").split('<30>')


# loop thru all lines and find line which have "Query" in it
count = 0
for x in allLogs:
    count += 1
    if x.find("query") > -1 and x.find(".lan") == -1:
        
        # Fix for when day is in single digit.....Dis what u get for using split so much nub
        x = x.replace("  ", " ")

        # When Query found...check next line to find NXDOMAIN 
        if allLogs[count].find("NXDOMAIN") > -1:
            x = x.replace("OpenWrt", "Blocked")
            name_convert()
            x = x.split(" ")

            # Create date
            x[0] = year + "-" + x[0] + "-" + x[1]

            insert.append((x[0],x[2],x[3],x[8],x[10]))
        else:
            x = x.replace("OpenWrt", "Allowed")
            name_convert()
            x = x.split(" ")

            # Create date
            x[0] = year + "-" + x[0] + "-" + x[1]

            insert.append((x[0],x[2],x[3],x[8],x[10]))


main.all_data(insert)
main.sort_data("Top_Allowed", "Domain", "WHERE Status = 'Allowed'")
main.sort_data("Top_Blocked", "Domain", "WHERE Status = 'Blocked'")
main.sort_data("Top_User", "User", "")
jsonTest =  {
    "TotalDomains": main.get_total_domain(),
    "TopUser": main.get_top_user(),
    "BlockedDomains": main.get_total_blocked(),
    "AllowedDomainsList": main.get_top_5("Top_Allowed"),
    "BlockedDomainsList": main.get_top_5("Top_Blocked"),
    "LastDomainsRequest": main.get_last_10_domain()

}
jsonTest = json.dumps(jsonTest, indent= 4)
j = open('stats.json', 'w')
sys.stdout = j
print(jsonTest)