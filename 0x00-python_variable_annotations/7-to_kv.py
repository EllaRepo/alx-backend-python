#!/usr/bin/env python3
"""Module that defines a function that takes a string k and
   an int OR float v as arguments and returns a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple
    Args:
        k: string
        v: integer/float
    Returns:
        A tuple
    """
    return k, v ** 2
