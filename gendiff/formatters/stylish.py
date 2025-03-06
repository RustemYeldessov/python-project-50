def stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    result = ['{']

    for item in diff:
        key = item['key']
        item_type = item['type']
        value = item.get('value')

        if item_type == 'nested':
            result.append(
                f"{indent}    {key}: {stylish(item['children'], depth + 1)}"
            )
        elif item_type == 'unchanged':
            result.append(
                f"{indent}    {key}: {to_str(value, depth + 1)}"
            )
        elif item_type == 'added':
            result.append(
                f"{indent}  + {key}: {to_str(value, depth + 1)}"
            )
        elif item_type == 'deleted':
            result.append(
                f"{indent}  - {key}: {to_str(value, depth + 1)}"
            )
        elif item_type == 'changed':
            result.append(
                f"{indent}  - {key}: "
                f"{to_str(item['old_value'], depth + 1)}"
            )
            result.append(
                f"{indent}  + {key}: "
                f"{to_str(item['new_value'], depth + 1)}"
            )

    result.append(indent + '}')
    return '\n'.join(result)


def to_str(value, depth):
    indent = ' ' * ((depth) * 4)
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {to_str(v, depth + 1)}")
        lines.append(indent + '}')
        return '\n'.join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return value