import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        dest='format',
        type=str,
        help='Set format of output'
    )
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)

def generate_diff(file_path1, file_path2):
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            data1 = json.load(file1)
            data2 = json.load(file2)

        def get_difference(data1, data2):
            result = {}
            for k, v in data1.items():
                if k in data2 and v == data2[k]:
                    result[f'  {k}'] = v
                else:
                    result[f'- {k}'] = v

            for k, v in data2.items():
                if k not in data1:
                    result[f'+ {k}'] = v
                elif k in data1 and v != data1[k]:
                    result[f'+ {k}'] = v
                elif k in data1 and v == data1[k]:
                    continue
            return result

        diff = get_difference(data1, data2)

        def format_diff(diff):
            sorted_data = dict(sorted(diff.items(), key=lambda x: x[0][2:]))
            print('{')
            for key, value in sorted_data.items():
                print(f"{key}: {value}")
            print('}')
        format_diff(diff)


if __name__ == '__main__':
    main()
