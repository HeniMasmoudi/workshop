"""
Sum & mean bad practice testing

"""

import numpy as np


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


def verify_sum():
    """check if the sum is exactly
    numpy sum"""
    values = np.array([3, 7, 1, 1])
    summ = sumofvalues(values)
    assert summ == 12


def verify_mean():
    """check if the mean is exactly
    numpy mean"""
    values = np.array([3, 7, 1, 1])

    meann = mean(values)
    assert meann == 3


if __name__ == "__main__":
    verify_sum()
    verify_mean()
