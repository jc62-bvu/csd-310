import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="G0league246@$^",
    database="pysports"
)

curse = db.cursor()

sql = "SELECT player.player_id, player.first_name, player.last_name, team.team_id, team.team_name \
    FROM player INNER JOIN team ON team.team_id=player.team_id"

curse.execute(sql)

myresult = curse.fetchall()

for x in myresult:
    print(x)