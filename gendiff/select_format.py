from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(format_name, data):
    if format_name == 'stylish':
        return stylish(data)
    elif format_name == 'plain':
        return plain(data)
    elif format_name == 'json':
        return json_formatter(data)
    else:
        raise ValueError(f"Unknown format: {format_name}")

