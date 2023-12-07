"""Module that defines a function that returns the sum of float/integer
    numbers in the list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of float/integer numbers in the list
    Args:
        mxd_lst: List of float and integer numbers
    Returns:
        The sum of float numbers
    """
    return sum(mxd_lst)
