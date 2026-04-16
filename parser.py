import requests
from bs4 import BeautifulSoup
import json

url = 'https://skyeng.ru/articles/samye-populyarnye-slova-v-anglijskom-yazyke/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Предположим, что таблицы с нужными словами — это все таблицы,
    # кроме тех, что содержат номер слова или другие признаки.
    # Здесь можно добавить более точную фильтрацию, если есть конкретные признаки.
    tables = soup.find_all('table')
    
    result_dict = {}
    
    for table in tables:
        # Можно фильтровать таблицы по признакам, если нужно
        # Например, пропускать таблицы с классом 'номер' или по другой логике
        # В данном примере берём все таблицы
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) >= 4:
                english_word = cells[1].get_text(strip=True)
                russian_word = cells[3].get_text(strip=True)
                result_dict[russian_word] = english_word
    
    # Сохраняем результат в JSON файл
    with open('words.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=4)
        
    print("Словарь успешно сохранен в файл words.json")
else:
    print(f"Не удалось загрузить страницу: статус {response.status_code}")