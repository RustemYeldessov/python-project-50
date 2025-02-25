def plain(diff, key_path=''):
    result = []
    sorted_keys = sorted(
        diff.keys(), key=lambda k: k[2:] if k.startswith(('- ', '+ ')) else k
    )
    processed_keys = set()

    for key in sorted_keys:
        value = diff[key]
        clean_key = key[2:] if key.startswith(('- ', '+ ')) else key
        new_path = f"{key_path}.{clean_key}" if key_path else clean_key

        if new_path in processed_keys:
            continue

        if isinstance(value, dict):
            if f"+ {clean_key}" in diff and f"- {clean_key}" in diff:
                old_value = diff[f"- {clean_key}"]
                new_value = diff[f"+ {clean_key}"]
                result.append(
                    f"Property '{new_path}' was updated. From "
                    f"{format_value(old_value)} to {format_value(new_value)}"
                )
                processed_keys.add(new_path)

            elif key.startswith('+ '):
                result.append(f"Property '{new_path}' "
                              f"was added with value: [complex value]")
                processed_keys.add(new_path)

            elif key.startswith('- '):
                result.append(f"Property '{new_path}' was removed")
                processed_keys.add(new_path)

            else:
                result.append(plain(value, new_path))

        else:
            if f"+ {clean_key}" in diff and f"- {clean_key}" in diff:
                old_value = diff[f"- {clean_key}"]
                new_value = diff[f"+ {clean_key}"]
                result.append(
                    f"Property '{new_path}' was updated. From "
                    f"{format_value(old_value)} to {format_value(new_value)}"
                )
                processed_keys.add(new_path)
            elif key.startswith('+ '):
                result.append(
                    f"Property '{new_path}' "
                    f"was added with value: {format_value(value)}"
                )
                processed_keys.add(new_path)

            elif key.startswith('- '):
                result.append(f"Property '{new_path}' was removed")
                processed_keys.add(new_path)

    return '\n'.join(result)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return value