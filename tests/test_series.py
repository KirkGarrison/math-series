from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_import():
    assert fibonacci
    assert lucas
    assert sum_series



def test_fibonacci_one():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_lucas_one():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_sum_series_one():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected