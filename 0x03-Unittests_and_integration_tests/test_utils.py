#!/usr/bin/env python3
"""
Unittest for utils methods
"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
import unittest
import requests
from unittest.mock import patch, Mock

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing access_nested_map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> Any:
        """ Test access_nested_map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> Any:
        """ Test access_nested_map_exception """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class for testing get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> Any:
        """ Test get_json """
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock(ok=True)
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Class for testing memoize """
    def test_memoize(self) -> Any:
        """ Test memoize """
        class TestClass:
            """ TestClass """
            def a_method(self):
                """ a_method """
                return 42

            @memoize
            def a_property(self):
                """ a_property """
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock:
            mock.return_value = 42
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
