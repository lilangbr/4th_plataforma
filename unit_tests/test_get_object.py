# You must be pytest installed in your machine
# See https://docs.pytest.org/en/stable/
# $ py.test name_of_file.py to run the test



from linkmodules.get_object import get_json


def test_get_json1():
    assert str(type(get_json('../src/image.json'))) == "<class 'list'>"
def test_get_json2():
    assert str(type(get_json('../src/vector.json'))) == "<class 'list'>"
