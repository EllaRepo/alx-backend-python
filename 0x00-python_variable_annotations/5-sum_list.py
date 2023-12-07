#!/usr/bin/env python3
"""Module that defines a function that returns the sum of float numbers in
   the list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of float numbers in the list
    Args:
        input_list: List of float numbers
    Returns:
        The sum of float numbers
    """
    return sum(input_list)
