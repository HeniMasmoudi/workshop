"""
scratch file for unittests workshop and

"""

import numpy as np
import pytest


@pytest.fixture(name="values", scope="module")
def fixture_values():
    """error margin"""
    vals = np.random.randint(0, 5, size=(10,))
    return vals


def sumofvalues(values):
    """iterate on values to compute the sum"""
    sum_ = 0
    for val in values:
        sum_ += val

    return sum_


def mean(values):
    """compute the mean using the first sum function"""
    average = sumofvalues(values) / len(values)
    return average


@pytest.fixture(name="sum_and_mean", scope="module")
def fixture_results(values):
    """fetch the sum and the mean for a given list of values"""
    summ = sumofvalues(values)
    meann = mean(values)
    return meann, summ


def test_sum(values, sum_and_mean):
    """check if the sum is exactly
    numpy sum"""
    _, summ = sum_and_mean
    assert summ == values.sum()


def test_mean(values, sum_and_mean):
    """check if the mean is exactly
    numpy mean"""
    meann, _ = sum_and_mean
    assert meann == values.mean()
