import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Canada",
    database="MCCDATA"
)

mycursor = mydb.cursor()

sql = "INSERT INTO testdata (memberkey,airhumidity,airtemperature) VALUES (%s, %s, %s)"
val = (1001,2454,8966)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
