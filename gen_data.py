import csv
import random
import os
from datetime import datetime, timedelta

# Функция для генерации синтетических данных
def generate_csv(file_path="data.csv", num_rows=1000,  min_quantity=1, max_quantity=50, min_price=10, max_price=100):

    # Список продуктов    
    products = [
        "яблоки", "груши", "сливы", "печенье", "конфеты Рот-Фронт", 
        "бананы", "ананасы", "молоко", "хлеб", "сыр", 
        "кефир", "сметана", "мандарины", "апельсины", "колбаса", 
        "шоколад", "картофель", "морковь", "капуста", "помидоры", 
        "огурцы", "сахар", "соль", "макароны", "рис"
    ]

    # Открытие файла для записи в формате CSV
    with open(file_path, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Заголовок столбцов
        writer.writerow(["product_name", "quantity", "price", "date"])

        # Генерация данных и запись в CSV-файл
        for _ in range(num_rows):
            item = random.choice(products)
            quantity = random.randint(min_quantity, max_quantity)
            price = random.randint(min_price, max_price)
            date = datetime.now() - timedelta(days=random.randint(0, 60))
            date_str = date.strftime("%Y-%m-%d")
            
            # Запись строки с данными
            writer.writerow([item, quantity, price, date_str])
            
    # Получение пути к файлу
    absolute_path = os.path.abspath(file_path)
    
    print(f"Файл {file_path} сгенерирован с {num_rows} строками данных. И находится по пути: {absolute_path}")

# Генерация датасета из 1000 наблюдений
generate_csv(file_path=r"your_path\data.csv", num_rows=1000)