#!/usr/bin/env python3
"""Module that defines a function that returns the first elements of
   a Sequence
"""
from typing import Mapping, TypeVar, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the first elements of a Sequence
    Args:
        lst: A of sequence
    Returns:
        the first element of the sequence if exits or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
