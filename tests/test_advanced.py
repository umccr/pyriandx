# -*- coding: utf-8 -*-

from .context import pyriandx

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def setUp(self):
        self.client = pyriandx.client()

    def test_url_helper(self):
        self.client.say_hi("nick")

if __name__ == '__main__':
    unittest.main()
