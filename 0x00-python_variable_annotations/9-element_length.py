#!/usr/bin/env python3
"""Module that defines a function that returns a list of tuples
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of sequence and integer
    Args:
        list: A list of sequence
    Returns:
        a list of tuples of sequence and integer
    """
    return [(i, len(i)) for i in lst]
