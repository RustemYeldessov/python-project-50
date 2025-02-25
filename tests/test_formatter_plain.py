import json

import pytest

from gendiff.gendiff_logic import generate_diff


@pytest.fixture
def file1():
    return {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }


@pytest.fixture
def file2():
    return {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }


@pytest.fixture
def expected_result():
    return """
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""


@pytest.fixture
def create_temp_files(tmpdir, file1, file2):
    file1_path = tmpdir.join("file1.json")
    file2_path = tmpdir.join("file2.json")

    with open(file1_path, "w") as f1:
        json.dump(file1, f1)

    with open(file2_path, "w") as f2:
        json.dump(file2, f2)

    return file1_path, file2_path


def test_generate_diff_with_plain(create_temp_files, expected_result):
    file1_path, file2_path = create_temp_files

    file1_path_str = str(file1_path)
    file2_path_str = str(file2_path)

    result = generate_diff(file1_path_str, file2_path_str, format_name='plain')

    assert result.strip() == expected_result.strip()