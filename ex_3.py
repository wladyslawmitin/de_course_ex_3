import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Путь к файлу с продажами
file_path = r"your_path\data.csv"

# Функция 1
# Принимает путь к файлу и возвращает список продаж в виде словарей 
def read_sales_data(file_path):

    with open(file_path,"r", encoding="utf-8") as file:
        
        reader = csv.reader(file)
        headers = next(reader)
        
        data_list = []
        
        # Проход цикла по строкам файла
        for row in reader:
            
            # Преобразование численных значений в int
            processed_row = [int(value) if value.isdigit() else value for value in row]
            
            # Преобразование даты из str в datetime
            row[3] = datetime.strptime(processed_row[3], "%Y-%m-%d").date()
            
            # Добавление словаря в список
            data_list.append(dict(zip(headers, processed_row)))

    return data_list

# Функция 2
# Принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж этого продукта.
def total_sales_per_product(sales_data):
    
    sales_per_product = dict()
    
    # Проход цикла по словарям
    for row in sales_data:
        
        # Определение названия продукта
        product_name = row['product_name']
        
        # Если продукт есть в словаре, прибавляем к его выручке новую сумму
        if product_name in sales_per_product:
            sales_per_product[product_name] += row['quantity']*row['price']
        else: 
        # Если продукта нет в словаре, добавляем его с первоначальной выручкой
            sales_per_product[product_name] = row['quantity']*row['price']
    
    return sales_per_product

# Функция 3
# Принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату.
def sales_over_time(sales_data):
    
    sales_per_date = dict()
    
    # тоже самое что и в предыдущей функции, только агрегация по дням
    for row in sales_data:
        date = row['date']
        if date in sales_per_date:
            sales_per_date[date] += row['quantity']*row['price']
        else: 
            sales_per_date[date] = row['quantity']*row['price']

    return sales_per_date

# Функция для определения товара с наибольшей выручкой
def highest_revenue_per_product(sales_data):
    
    # Получаем список с словарями выручки по каждому товару
    sales_per_product = total_sales_per_product(sales_data)
    
    # Находим максимальную выручку
    max_revenue = max(sales_per_product.values())
    
    # Возвращаем продукты с максимальной выручкой
    return {product_name: revenue for product_name, revenue in sales_per_product.items() if revenue == max_revenue}

# Функция для определения дня с наибольшей выручкой (аналогична предыдущей)
def highest_revenue_per_day(sales_data):
    
    sales_per_day = sales_over_time(sales_data)
    
    max_revenue = max(sales_per_day.values())
    
    return {date: revenue for date, revenue in sales_per_day.items() if revenue == max_revenue}

# Функция для построения графика выручки по каждому продукту
def plot_revenue_per_product(data_sales):
    plt.figure(figsize=(24, 8))
    plt.bar(list(data_sales.keys()), list(data_sales.values()), color='indigo', alpha = 0.7)
    plt.xlabel('Продукты')
    plt.ylabel('Выручка')
    plt.title('Выручка по продуктам')
    plt.xticks(rotation=45)    
    plt.show()

# Функция для построения графика выручки по дням
def plot_revenue_per_day(data_sales):
    plt.figure(figsize=(24, 8))
    plt.bar(list(data_sales.keys()), list(data_sales.values()), color='indigo', alpha = 0.7)
    plt.xlabel('Дата')
    plt.ylabel('Выручка')
    plt.title('Выручка по датам')
    plt.xticks(rotation=45)
    plt.show()

data = read_sales_data(file_path)

# Выручка по каждому продукту
revenue_per_product = total_sales_per_product(data)
# print(total_sales_per_product)

# Выручка по дням
revenue_per_day = sales_over_time(data)
# print(revenue_per_day)

# Продукт, принесший наибольшую выручку 
print(f'Продукт с наибольшей выручкой:\n{highest_revenue_per_product(data)}')

# День, в которые была наибольшая выручка
print(f'День с наибольшей выручкой:\n{highest_revenue_per_day(data)}')

# График выручки по каждому продукту
plot_revenue_per_product(revenue_per_product)

# График выручки по дням
plot_revenue_per_day(revenue_per_day)