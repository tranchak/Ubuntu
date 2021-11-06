import psycopg2

conn = psycopg2.connect(dbname='Oleg', user='Oleg', password='1988', host='localhost')

cursor = conn.cursor()  # создаем обьект курсора

sql = '''CREATE TABLE less2
(
    Id SERIAL PRIMARY KEY,
    FirstName CHARACTER VARYING(20),
    LastName CHARACTER VARYING(20),
    Email CHARACTER VARYING(30) UNIQUE,
    Phone CHARACTER VARYING(30) UNIQUE,
    Age INTEGER

    );'''

cursor.execute(sql)  # вставляем SQl код
conn.commit()  # делаем commit
conn.close()
