import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="crypto"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM blockchain")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)