def stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    result = ['{']

    sorted_keys = sorted(diff.keys(), key=lambda k: k[2:] if k.startswith(('- ', '+ ', '  ')) else k)

    for key in sorted_keys:
        value = diff[key]
        is_added_or_removed = key.startswith(('+ ', '- '))
        clean_key = key[2:] if is_added_or_removed else key

        if isinstance(value, dict):
            if is_added_or_removed:
                result.append(f"{indent}  {key}: {{")
                sub_indent = indent + " " * 4
                for sub_key, sub_value in value.items():
                    formatted_value = format_value(sub_value, depth + 2)
                    result.append(f"{sub_indent}    {sub_key}: {formatted_value}")
                result.append(f"{indent}    }}")

            else:
                result.append(f"{indent}    {clean_key}: {stylish(value, depth + 1)}")
        else:
            if key.startswith(('+ ', '- ')):
                result.append(f"{indent}  {key}: {format_value(value, depth + 1)}")
            else:
                result.append(f"{indent}    {key}: {format_value(value, depth + 1)}")

    result.append(indent + '}')
    result = [line.rstrip() for line in result]
    return '\n'.join(result)

def format_value(value, depth):
    if isinstance(value, dict):
        return stylish(value, depth)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return value