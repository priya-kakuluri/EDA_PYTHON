import pytest
from logicgates import AND, OR, NOT ,NAND ,NOR ,XOR ,XNOR

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (0, 1, 0),
    (1, 0, 0),
    (1, 1, 1),
])
def test_and(a, b, expected):
    assert AND(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1),
])
def test_OR(a, b, expected):
    assert OR(a, b) == expected

@pytest.mark.parametrize("a, expected", [
    (0, 1),
    (1, 0)
])
def test_NOT(a, expected):
    assert NOT(a) == expected

@pytest.mark.parametrize("a,b,expected",[
    (0,0,1),
    (0,1,1),
    (1,0,1),
    (1,1,0)
])
def test_NAND(a,b,expected):
    assert NAND(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (1,1,0)
])
def test_NOR(a,b,expected):
    assert NOR(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (0,0,0),
    (0,1,1),
    (1,0,1),
    (1,1,0)
])
def test_XOR(a,b,expected):
    assert XOR(a,b)==expected

@pytest.mark.parametrize("a,b,expected",[
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (1,1,1)
])
def test_XNOR(a,b,expected):
    assert XNOR(a,b)==expected


