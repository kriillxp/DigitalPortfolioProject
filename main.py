import mysql.connector
from config import host, user, password, database
mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database=database
)
mydb.autocommit = True
mycursor = mydb.cursor()

mycursor.execute("INSERT INTO user (login, password) VALUE ('GG@mail.ru', '126');")
mydb.commit()
mydb.close()