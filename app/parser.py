import json

# Функция для чтения JSON файла и записи данных в текстовый файл
def parse_json_to_txt(json_file, txt_file):
    try:
        # Открываем JSON файл и загружаем данные
        with open(json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

        # Открываем текстовый файл для записи
        with open(txt_file, 'w', encoding="utf-8-sig") as f:
            # Проходим по ключам и значениям в словаре
            for key, value in data.items():
                f.write(f"{key}: {value}\n")

        print(f"Данные успешно перенесены из {json_file} в {txt_file}.")

    except FileNotFoundError:
        print(f"Файл {json_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Укажите имена файлов
txt_file = 'C:/Users/alium/OneDrive/Рабочий стол/github_project_clone/output.txt'
json_file = 'C:/Users/alium/OneDrive/Рабочий стол/github_project_clone/org_data.json'


# Вызов функции
parse_json_to_txt(json_file, txt_file)
