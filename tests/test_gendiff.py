import unittest
from gendiff.scripts.gendiff import main
from gendiff.scripts.gendiff import generate_diff


def test_gendiff() -> dict:

    json1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    json2 = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }

    expected_result = {
        "- follow": False,
        "host": "hexlet.io",
        "- proxy": "123.234.53.22",
        "- timeout": 50,
        "+ timeout": 20,
        "+ verbose": True
    }

    result = generate_diff(json1, json2)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"