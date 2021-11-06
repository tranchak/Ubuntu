import psycopg2

conn = psycopg2.connect(dbname='Oleg', user='Oleg', password='1988', host='localhost')

cursor = conn.cursor() # создаем обьект курсора

sql = '''CREATE TABLE Che
(
    LastName CHARACTER VARYING(20),
    Age INTEGER CHECK (Age >18),
    Email CHARACTER VARYING(30) UNIQUE CHECK(Email !='')
    
   );'''

cursor.execute(sql)  # вставляем SQl код
conn.commit()  # делаем commit
conn.close()