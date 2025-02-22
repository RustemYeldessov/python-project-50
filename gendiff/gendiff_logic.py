import yaml
import argparse
import json
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        dest='format',
        type=str,
        default='stylish',
        help='Set format of output'
    )
    return parser.parse_args()

def load_file(file_path):
    file_path_str = str(file_path)
    try:
        with open(file_path_str, 'r') as file:
            if file_path_str.endswith('.json'):
                return json.load(file)
            elif file_path_str.endswith(('.yml', '.yaml')):
                return yaml.safe_load(file)
            else:
                raise ValueError(f"Неизвестный формат файла: {file_path}")
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден!")
        exit(1)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"Ошибка: не удалось загрузить файл {file_path}: {e}")
        exit(1)

def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = get_difference(data1, data2)

    formatters = {
        'stylish': stylish,
        'plain': plain
    }
    if format_name not in formatters:
        raise ValueError(f"Unknown fomat: {format_name}")

    formatter = formatters[format_name]
    return formatter(diff)


def get_difference(data1, data2):
    result = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            if key in data1 and key in data2:
                result[f'{key}'] = get_difference(value1, value2)
        elif key in data1 and key in data2:
            if value1 != value2:
                result[f'- {key}'] = value1
                result[f'+ {key}'] = value2
            else:
                result[f'{key}'] = value1
        elif key in data1 and key not in data2:
            result[f'- {key}'] = value1
        elif key in data2 and key not in data1:
            result[f'+ {key}'] = value2

    return result

