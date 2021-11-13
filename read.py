import pandas as pd

df = pd.read_excel(r'/home/dima/Загрузки/Telegram Desktop/с_ценами_Татьяна_380645_СПЕЦИФИКАЦИЯ_003_04_08_2021.xlsx')

print(df[['Артикул','Наименование номенклатуры']])