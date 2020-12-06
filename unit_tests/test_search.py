# You must be pytest installed in your machine
# See https://docs.pytest.org/en/stable/
# $ py.test name_of_file.py to run the test



from linkmodules.search import search_element

matrix_example = [[2, 5, 0, 1, 2, 12, 4], [0, 3, 0, 14, 5, 0, 8], [15, 15, 2, 8, 7, 2, 14]]
mt = matrix_example
m = len(mt)
n = len(mt[0])

def test_search0():
    assert search_element(0, mt, m, n) == 4
def test_search1():
    assert search_element(1, mt, m, n) == 1
def test_search_neg():
    assert search_element(-10, mt, m, n) == 0
def test_search12():
    assert search_element(12, mt, m, n) == 1
def test_search1000():
    assert search_element(1000, mt, m, n) == 0
def test_search4():
    assert search_element(4, mt, m, n) == 1
def test_search2():
    assert search_element(2, mt, m, n) == 4


