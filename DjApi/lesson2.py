import sqlite3
# import time

conn = sqlite3.connect('db.sqlite3') #cоздает соединение с БД.
cursor = conn.cursor() #подготовка запроса с SQL ставим курсор для работы
SQL ='''INSERT INTO main_auto ('id', 'name', 'price', 'brand_id')
    VALUES (5, 'A8', 65, 2)
'''
# print(dir(conn), 'object cursor')
c=cursor.execute(SQL) #Выполнить запрос по SQL
# time.sleep(10)
# print(dir(c))
# print(cursor.fetchall())
conn.commit()
# conn.close()