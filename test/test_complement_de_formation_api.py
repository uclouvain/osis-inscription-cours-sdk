"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.13
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api.complement_de_formation_api import ComplementDeFormationApi  # noqa: E501


class TestComplementDeFormationApi(unittest.TestCase):
    """ComplementDeFormationApi unit test stubs"""

    def setUp(self):
        self.api = ComplementDeFormationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_complement_de_formation(self):
        """Test case for get_complement_de_formation

        """
        pass


if __name__ == '__main__':
    unittest.main()
