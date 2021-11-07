import psycopg2

conn = psycopg2.connect(dbname='Oleg', user='Oleg', password='1988', host='localhost')

cursor = conn.cursor()  # создаем обьект курсора

sql = '''CREATE TABLE dz
(
    Id PRIMARY KEY,


    );'''

cursor.execute(sql)  # вставляем SQl код
conn.commit()  # делаем commit
conn.close()
