"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.13
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api.mini_formation_api import MiniFormationApi  # noqa: E501


class TestMiniFormationApi(unittest.TestCase):
    """MiniFormationApi unit test stubs"""

    def setUp(self):
        self.api = MiniFormationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enroll_mini_formation(self):
        """Test case for enroll_mini_formation

        """
        pass

    def test_inscriptions_mini_formations(self):
        """Test case for inscriptions_mini_formations

        """
        pass

    def test_mini_formations_inscriptibles(self):
        """Test case for mini_formations_inscriptibles

        """
        pass

    def test_unenroll_mini_formation(self):
        """Test case for unenroll_mini_formation

        """
        pass


if __name__ == '__main__':
    unittest.main()
