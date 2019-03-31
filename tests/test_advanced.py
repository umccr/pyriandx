# -*- coding: utf-8 -*-


import random
import unittest

from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none
from requests import Session

from .context import pyriandx


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""
     
    # @patch('pyriandx.core.requests_retry_session.post')
    # def test_create_case(self,mock_get):
    #     mock_get.return_value.ok = True
    #     accession_number = 12345
    #     data = {}
    #     data["accessionNumber"] = accession_number
    #     res = self.client.create_case(data)


    @patch.object(Session, 'post')
    def test_create_case(self,mock_get):
        fake_response = [{
            'id': 1111,
            'accessionNumber': 12345,
            'dateCreated':'2019-03-30'
        }]

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a list of todos.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = fake_response


        client = pyriandx.client(
        email="nick.clark@unimelb.edu.au",
        baseURL="https://httpbin.org/anything",
        key="password",
        institution="institution"
        )


        # Call the service, which will send a request to the server.
        accession_number = 12345
        data = {}
        data["accessionNumber"] = accession_number
        res = client.create_case(data)

        # # If the request is sent successfully, then I expect a response to be returned.
        # assert_list_equal(response.json(), todos)

if __name__ == '__main__':
    unittest.main()
