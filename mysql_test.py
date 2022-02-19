import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="G0league246@$^",
    database="pysports"
)

mycursor = db.cursor()

