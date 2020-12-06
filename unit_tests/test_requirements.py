# You must be pytest installed in your machine
# See https://docs.pytest.org/en/stable/
# $ py.test name_of_file.py to run the test



from linkmodules.requirements import vector_requirements as v_req
from linkmodules.requirements import matrix_requirements as m_req

matrix_ok = [[2, 5, 0, 1, 2, 12, 4], [0, 3, 0, 14, 5, 0, 8], [15, 15, 2, 8, 7, 2, 14]]
matrix_wrong1 = 4
matrix_wrong2 = []
matrix_wrong3 = [[]]

vector_ok = [1, 3, 0, 15]
vector_wrong1 = [1, 28, 0, 0]
vector_wrong2 = []
vector_wrong3 = [[1, 28, 0, 0]]
vector_wrong4 = 4


def test_matrix0():
    assert m_req(matrix_ok) == 1
def test_matrix1():
    assert m_req(matrix_wrong1) == 0
def test_matrix2():
    assert m_req(matrix_wrong2) == 0
def test_matrix3():
    assert m_req(matrix_wrong3) == 0


def test_vector0():
    assert v_req(vector_ok) == 1
def test_vector1():
    assert v_req(vector_wrong1) == 0
def test_vector2():
    assert v_req(vector_wrong2) == 0
def test_vector3():
    assert v_req(vector_wrong3) == 0
def test_vector4():
    assert v_req(vector_wrong4) == 0
