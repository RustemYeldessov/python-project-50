from gendiff.formatters.json import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def get_formatter(format_name):
    if format_name == 'stylish':
        return stylish
    elif format_name == 'plain':
        return plain
    elif format_name == 'json':
        return json_formatter
    else:
        raise ValueError(f"Unknown format: {format_name}")

