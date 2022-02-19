import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="G0league246@$^",
    database="pysports"
)

curse = db.cursor()

curse.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = curse.fetchall()

mycursor = db.cursor()

mycursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = mycursor.fetchall()

for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))


    


