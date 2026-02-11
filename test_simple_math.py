import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square_positive(simple_math):
    result = simple_math.square(2)
    assert result == 4

def test_square_negative(simple_math):
    result = simple_math.square(-3)
    assert result == 9


def test_square_zero(simple_math):
    result = simple_math.square(0)
    assert result == 0

def test_cube_positive(simple_math):
    result = simple_math.cube(3)
    assert result == 27

def test_cube_negative(simple_math):
    result = simple_math.cube(-3)
    assert  result == -27

def test_cube_zero(simple_math):
    result = simple_math.cube(0)
    assert result == 0

















