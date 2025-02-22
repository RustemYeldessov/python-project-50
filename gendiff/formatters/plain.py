def plain(diff, key_path):

    sorted_keys = sorted(diff.keys(), key=lambda k: k[2:] if k.startswith(('- ', '+ ')) else k)
    result = ''

    for key in sorted_keys:
        value = diff[key]
        clean_key = key[2:]

        is_added = f"+ {clean_key}" in diff
        is_removed = f"- {clean_key}" in diff
        is_changed = not key.startswith('+ ') and not key.startswith('- ')

        key_path = ''

        if isinstance(value, dict):
            if f"+ {clean_key}" in sorted_keys and not f"- {clean_key}" in sorted_keys:
                key_path += f'{key_path}{key}.'
                result += plain(value, key_path='')
            elif f"- {clean_key}" in sorted_keys and not f"+ {clean_key}" in sorted_keys:
                result += f"Property '{key[2:]}' was removed\n"
            elif is_changed:
                key_path += f'{key_path}{key}.'
                result += plain(value, key_path='')
        else:
            if f"+ {clean_key}" in sorted_keys and f"- {clean_key}" not in sorted_keys:
                key_path = f'{key_path}{key}'
                result += f"Property '{key_path} was added with value: {value}\n"
            elif f"- {clean_key}" in sorted_keys and f"+ {clean_key}" not in sorted_keys:
                key_path = f'{key_path}{key}'
                result += f"Property '{key_path} was removed\n"
            elif f"+ {clean_key}" in sorted_keys and f"- {clean_key}" in sorted_keys:

                old_value = diff[f"- {clean_key}"]
                new_value = diff[f"+ {clean_key}"]

                key_path = f'{key_path}{key}'
                result += f"Property '{key_path} was updated. From {old_value} to {new_value}\n"
            else:
                result += 'Fuck yourself motherfucker\n'

    print(result)
    return result
