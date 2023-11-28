def test_uppercase_single_word():
    assert "computer".upper() == "COMPUTER"


def say_hello():
    print("Hello!!!!!!")


def test_uppercase_two_words():
    assert "computer name".upper() == "COMPUTER NAME"


def test_reversed_int_list():
    example = [1,2,3,4,5]
    expected_answer = [5,4,3,2,1]
    assert list(reversed(example)) == expected_answer

import numpy as np

def test_squaring():
    """Test calculating the element-wise square of an array"""
    a = np.array([1., 2., 3.])
    a_squared = np.array([1., 4., 9.])
    # assert all(a**2 == a_squared)
    np.testing.assert_array_almost_equal(a**2, a_squared)

def test_almost_equaual_floats_numpy():
    assert np.isclose(1.2-1.0, 0.2)


def test_almost_equaual_floats():
    assert not 1.2-1.0 == 0.2

def test_sum_floating_non_base_2_addition_numpy():
    a = np.array([1.2, -1.0])
    assert not a.sum() == 0.2


def test_sum_floating_non_base_2_addition():
    a = [1.2, -1.0]
    assert not sum(a) == 0.2


def test_sum_floating_base_2_addition_numpy():
    a = np.array([1.5, -1.0])
    assert a.sum() == 0.5

