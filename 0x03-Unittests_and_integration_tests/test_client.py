#!/usr/bin/env python3
"""
Unittests for client.GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, param

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """
    @parameterized.expand([
        param(org_name='google',
              resource="https://api.github.com/orgs/google"),
        param(org_name='abc',
              resource="https://api.github.com/orgs/abc")
    ])
    @patch('client.get_json')
    def test_org(self, mock_get_json, org_name, resource):
        """ Test GithubOrgClient.org """
        mock_get_json.return_value = True
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, True)
        mock_get_json.assert_called_once_with(resource)

    def test_public_repos_url(self):
        """ Test GithubOrgClient._public_repos_url """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = True
            client = GithubOrgClient('google')
            self.assertEqual(client._public_repos_url, True)
            mock_public_repos_url.assert_called_once_with()

    @patch('client.get_json')
    def test_public_repos(self, mock_getJson):
        """ Test GithubOrgClient.public_repos """
        test_choice = [{"name": "repo1", "license": {"key": "my_license"}},
                       {"name": "repo2"}]

        mock_getJson.return_value = test_choice
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            url = 'https://api.github.com/orgs/abc/repos'
            mock_public_repos_url.return_value = url
            client = GithubOrgClient('google')
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_getJson.assert_called_once_with(url)
            mock_public_repos_url.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test GithubOrgClient.has_license """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)
