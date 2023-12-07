#!/usr/bin/env python3
"""Module that defines a function that returns the first elements of
   a Sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first elements of a Sequence
    Args:
        lst: A of sequence
    Returns:
        the first element of the sequence if exits or None
    """
    if lst:
        return lst[0]
    else:
        return None
