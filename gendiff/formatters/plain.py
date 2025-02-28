def plain(diff, key_path=''):
    result = []

    for item in diff:
        key = item['key']
        item_type = item['type']
        new_path = f"{key_path}.{key}" if key_path else key

        if item_type == 'nested':
            result.append(plain(item['children'], new_path))
        elif item_type == 'added':
            value = format_value(item['value'])
            result.append(f"Property '{new_path}' was added with value: {value}")
        elif item_type == 'deleted':
            result.append(f"Property '{new_path}' was removed")
        elif item_type == 'changed':
            old_value = format_value(item['old_value'])
            new_value = format_value(item['new_value'])
            result.append(f"Property '{new_path}' was updated. From {old_value} to {new_value}")

    return '\n'.join(filter(None, result))


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return value