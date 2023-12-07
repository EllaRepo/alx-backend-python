#!/usr/bin/env python3
"""Module that defines a function that takes a float multiplier and returns
   a function that multiply argument bu the multiplier and return the result
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Define a function that takes a float argument and returns a float
    Args:
        multiplier: a float number
    Returns:
        a function
    """
    def multiply(x: float) -> float:
        """Multiply the argument by the multiplier and return the result
        Args:
            x: a float number
        Returns:
            the product of a number with a multiplier
        """
        return x * multiplier

    return multiply
