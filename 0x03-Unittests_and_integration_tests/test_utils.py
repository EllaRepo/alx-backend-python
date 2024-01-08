#!/usr/bin/env python3
"""Unit test module for utils module.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """Test function for utils.access_nested_map
        Args:
            nested_map (dict): A dictionary that may have nested dictionaries
            path (List, tuple, set): Keys to get to the required value in the
                                     nested dictionary
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
