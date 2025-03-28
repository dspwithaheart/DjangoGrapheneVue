#!/usr/bin/env python

"""Tests for `{{cookiecutter.project_slug}}` package."""

import pytest
import unittest


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_test():
    assert True


# def test_content():
#     """Sample pytest test function"""
#
#     answer = {{cookiecutter.project_slug}}.get_the_answer("WTF?")
#     assert answer == "42"
#
#
# class Test{{cookiecutter.project_slug.title()}}(unittest.TestCase):
#     """ unittest TestClass for `{{cookiecutter.project_slug}}` package."""
#
#     def setUp(self):
#         """Set up test fixtures, if any."""
#
#     def tearDown(self):
#         """Tear down test fixtures, if any."""
#
#     def test_something(self):
#         """Test something."""
#         answer = {{cookiecutter.project_slug}}.get_the_answer("WTF?")
#         self.assertEqual("42" , answer)
