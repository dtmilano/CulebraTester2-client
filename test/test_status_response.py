# coding: utf-8

"""
    CulebraTester

    ## Snaky Android Test --- If you want to be able to try out the API using the **Execute** or **TRY** button from this page - an android device should be connected using `adb` - the server should have been started using `./culebratester2 start-server`  then you will be able to invoke the API and see the responses.   # noqa: E501

    OpenAPI spec version: 2.0.73
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import culebratester_client
from culebratester_client.models.status_response import StatusResponse  # noqa: E501
from culebratester_client.rest import ApiException


class TestStatusResponse(unittest.TestCase):
    """StatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStatusResponse(self):
        """Test StatusResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = culebratester_client.models.status_response.StatusResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
