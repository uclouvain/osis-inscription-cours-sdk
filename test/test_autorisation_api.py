"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.5
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api.autorisation_api import AutorisationApi  # noqa: E501


class TestAutorisationApi(unittest.TestCase):
    """AutorisationApi unit test stubs"""

    def setUp(self):
        self.api = AutorisationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_est_autorise(self):
        """Test case for get_est_autorise

        """
        pass


if __name__ == '__main__':
    unittest.main()
