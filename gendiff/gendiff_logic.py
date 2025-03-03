from gendiff.get_tree import get_tree
from gendiff.load_data import load_file
from gendiff.select_format import get_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    diff = get_tree(data1, data2)

    formatter = get_formatter(format_name)
    return formatter(diff)
