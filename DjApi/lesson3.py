import psycopg2

conn = psycopg2.connect(dbname='tdv', user='tdv', password='123', host='localhost')

cursor = conn.cursor() # создаем обьект курсора

sql = '''SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name in ('Лада'));
'''
sql2 = '''SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name ='Лада' or name='БМВ');
'''
sql3 = '''SELECT * FROM main_auto WHERE brand_id in (SELECT ID FROM main_brand WHERE name NOT IN ('Лада'));
'''
sql4 = '''SELECT * FROM main_auto WHERE price BETWEEN 15 AND 50;
'''
sql5 = '''SELECT * FROM main_auto WHERE name LIKE 'Гра%';
'''
#sql6 = '''SELECT round(AVG(price),2) AS avg_price FROM main_auto;
#'''
sql7 = '''SELECT STRING_AGG (name,' ') FROM main_auto;
'''
sql8 = '''SELECT brand_id, COUNT(*) AS ModelCount FROM main_auto GROUP BY brand_id ORDER BY count(brand_id);
'''

# cursor.execute(sql)  # вставляем SQl код
# cursor.execute(sql2)  # вставляем SQl код
# cursor.execute(sql3)  # вставляем SQl код
# cursor.execute(sql4)  # вставляем SQl код
# cursor.execute(sql5)  # вставляем SQl код
#cursor.execute(sql6)  # вставляем SQl код
#cursor.execute(sql7)  # вставляем SQl код
cursor.execute(sql8)  # вставляем SQl код
print(cursor.fetchall())
conn.commit()  # делаем commit
conn.close()