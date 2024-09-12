import matplotlib.pyplot as plt
import pandas as pd
from task_1 import data


""" Преобразование колонки 'Sales' в числовой тип """
data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')

""" Удаление строк с NaN в колонке 'Sales' в копии"""
data = data.dropna(subset=['Sales']).copy()

""" Определение групп продаж на основе квантилей """
data.loc[:, 'Sale_group'] = pd.qcut(data['Sales'], 3, labels=["Низкие продажи",
                                                              "Средние продажи",
                                                              "Высокие продажи"])

""" Группировка по региону и группе продаж с явным указанием observed=False """
sales_by_region_group = data.groupby(['Region', 'Sale_group'], observed=False)['Sales'].sum().unstack()

""" Визуализация """
sales_by_region_group.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Распределение продаж по регионам и группам продаж')
plt.show()
