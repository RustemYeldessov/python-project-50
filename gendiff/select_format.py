from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(format_name):
    formatters = {
        'stylish': stylish,
        'plain': plain,
        'json': json_formatter
    }
    if format_name not in formatters:
        raise ValueError(f"Unknown format: {format_name}")

    return formatters[format_name]