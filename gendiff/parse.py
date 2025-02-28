import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        dest='format',
        type=str,
        default='stylish',
        help='Set format of output'
    )
    return parser.parse_args()