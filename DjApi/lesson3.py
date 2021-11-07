import psycopg2

conn = psycopg2.connect(dbname='tdv', user='tdv', password='123', host='localhost')

cursor = conn.cursor() # создаем обьект курсора

# sql = '''SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name in ('Лада'));
# '''
# sql2 = '''SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name ='Лада' or name='БМВ');
# '''
sql3 = '''SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name NOT IN ('Лада'));
'''
cursor.execute(sql3)  # вставляем SQl код
print(cursor.fetchall())
conn.commit()  # делаем commit
conn.close()