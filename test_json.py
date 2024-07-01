import json


def test_load_json_from_string():
    assert ["abc", True, False] == json.loads('["abc", true, false]')
