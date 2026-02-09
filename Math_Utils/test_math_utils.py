import pytest
from math_utils import sum_list, square, factorial

def test_sum_list():
    assert sum_list([2,3,4]) == 9
    assert sum_list([]) == 0

def test_square():
    assert square(4) == 16
    assert square(0) == 0

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

    with pytest.raises(ValueError):
        assert factorial(-1)