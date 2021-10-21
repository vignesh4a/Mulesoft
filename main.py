import sqlite3

connection = sqlite3.connect('Movies.db')
cursor = connection.cursor()

connection.execute('CREATE TABLE Movie(Movie TEXT, Actor TEXT, Actress CHAR(50),Year REAL);')

cursor.execute("INSERT INTO Movie (Movie,Actor,Actress,Year) VALUES ('3-Idiots','Aamir Khan','Kareena Kapoor',2009)")
cursor.execute("INSERT INTO Movie (Movie,Actor,Actress,Year) VALUES ('Shershaah','Sidharth Malhotra','Kiara Advani',2021)")
cursor.execute("INSERT INTO Movie (Movie,Actor,Actress,Year) VALUES ('The Man Who Knew Infinity ','Dev Patel','Devika Bhise',2016)")

data = connection.execute("select * from Movie")

for row in data:
    print("Movie : "+row[0],"Actor : "+row[1],"Actress : "+row[2],"Year : "+str(row[3]),sep="\n",end="\n======================\n")

connection.commit()
connection.close()
