import pandas as pd
import datetime


""" Загрузка данных из Google Sheets """
sheet_url = "https://docs.google.com/spreadsheets/d/1DkdhWMrVjtflQfmCIKl8hCjSlIxph1L42_fgyFo0QPs/export?format=csv"
data = pd.read_csv(sheet_url)

""" Вывод первых строк данных """
data.head()

""" Группировка по подгруппе товаров за все время """
top_subcategories_all_time = data['Sub-Category'].dropna().value_counts().head(4)

""" Визуализация за все время"""
if not data.empty:
    top_subcategories_all_time.plot(kind='bar', title='Топ-4 подгруппы товаров за все время')
else:
    print("Нет данных за все время.")

""" Текущая дата """
current_date = datetime.datetime.now()

""" Фильтр за последние 2 года """
last_two_years = current_date - pd.DateOffset(years=2)
data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True)
data_last_two_years = data[data['Order Date'] >= last_two_years]

top_subcategories_last_two_years = data_last_two_years['Sub-Category'].value_counts().head(4)

""" Визуализация за последние 2 года"""
if not data_last_two_years.empty:
    top_subcategories_last_two_years = data_last_two_years['Sub-Category'].value_counts().head(4)
    top_subcategories_last_two_years.plot(kind='bar', title='Топ-4 подгруппы товаров за последние два года')
else:
    print("Нет данных за последние два года.")


""" Фильтр за последний год """
last_one_year = current_date - pd.DateOffset(years=1)
data_last_one_year = data[(data['Order Date']) >= last_one_year]

top_subcategories_last_one_year = data_last_one_year['Sub-Category'].value_counts().head(4)

""" Визуализация последнего года"""
if not data_last_two_years.empty:
    top_subcategories_last_one_years = data_last_one_year['Sub-Category'].value_counts().head(4)
    top_subcategories_last_one_year.plot(kind='bar', title='Топ-4 подгруппы товаров за последний год')
else:
    print("Нет данных за последний год.")
