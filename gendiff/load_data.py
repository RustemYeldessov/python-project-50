import json
import yaml


def parse_data(data, format_name):
    if format_name == 'json':
        return json.loads(data)
    elif format_name in ('yml', 'yaml'):
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Неизвестный формат данных: {format_name}")


def load_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            extension = file_path.split('.')[-1]
            return parse_data(data, extension)
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден!")
        exit(1)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Ошибка: не удалось загрузить файл {file_path}: {e}")
        exit(1)