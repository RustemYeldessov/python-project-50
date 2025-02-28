def get_difference(data1, data2):
    result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            result.append({
                'key': key,
                'type': 'nested',
                'children': get_difference(value1, value2)
            })
        elif key in data1 and key in data2:
            if value1 != value2:
                result.append({
                    'key': key,
                    'type': 'changed',
                    'old_value': value1,
                    'new_value': value2
                })
            else:
                result.append({
                    'key': key,
                    'type': 'unchanged',
                    'value': value1
                })
        elif key in data1:
            result.append({
                'key': key,
                'type': 'deleted',
                'value': value1
            })
        elif key in data2:
            result.append({
                'key': key,
                'type': 'added',
                'value': value2
            })

    return result