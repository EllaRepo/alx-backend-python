#!/usr/bin/env python3
"""Unit test module for utils module.
"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)


class TestGithubOrgClient(unittest.TestCase):
    """Unit test class for client.GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fn: MagicMock) -> None:
        """Unit Test for org method.
        """
        mocked_fn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
