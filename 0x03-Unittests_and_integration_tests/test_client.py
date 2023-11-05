#!/usr/bin/env python3
"""
Unittests for client.GithubOrgClient class
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, param, parameterized_class
import client
from fixtures import TEST_PAYLOAD

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


@parameterized_class(
    ["org_payload", "repos_payload", "expected_repos", "apache2_repos"],
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient.public_repos """
    @classmethod
    def setUpClass(cls):
        """Set up for the integration test"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == "https://api.github.com/orgs/{org}":
                return Mock(ok=True, json=lambda: cls.org_payload)
            if url == cls.org_payload["repos_url"]:
                return Mock(ok=True, json=lambda: cls.repos_payload)

        cls.mock_get.side_effect = side_effect

    def test_public_repos(self):
        """ Test GithubOrgClient.public_repos without license """
        self.assertEqual(GithubOrgClient('google').public_repos(),
                         self.expected_repos,)

    def test_public_repos_with_license(self):
        """ Test GithubOrgClient.public_repos with license """
        self.assertEqual(GithubOrgClient('google').public_repos('apache-2.0'),
                         self.apache2_repos,)

    @classmethod
    def tearDownClass(cls):
        """Tear down for the integration test"""
        cls.get_patcher.stop()
