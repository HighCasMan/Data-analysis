from task_1 import data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

""" Построение boxplot для продаж """
plt.figure(figsize=(10, 6))
sns.boxplot(data['Sales'])
plt.title('Boxplot для продаж')
plt.show()

""" Удаление выбросов по правилу 3 сигм """
data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')
mean_sales = data['Sales'].mean()
std_sales = data['Sales'].std()

""" Фильтр данных без аномалий """
filtered_sales = data[(data['Sales'] >= mean_sales - 3*std_sales) & (data['Sales'] <= mean_sales + 3*std_sales)]

""" Повторное построение boxplot без аномалий """
plt.figure(figsize=(10, 6))
sns.boxplot(filtered_sales['Sales'])
plt.title('Boxplot для продаж без аномалий')
plt.show()
