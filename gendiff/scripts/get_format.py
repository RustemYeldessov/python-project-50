def formatted(diff):
    sorted_data = dict(sorted(diff.items(), key=lambda x: x[0][2:]))

    formatted_result = ['{']
    for key, value in sorted_data.items():
        formatted_result.append(f"{key}: {value}")
    formatted_result.append('}')
    return '\n'.join(formatted_result)