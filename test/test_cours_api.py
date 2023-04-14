"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.7
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api.cours_api import CoursApi  # noqa: E501


class TestCoursApi(unittest.TestCase):
    """CoursApi unit test stubs"""

    def setUp(self):
        self.api = CoursApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_desinscrire_aun_cours(self):
        """Test case for desinscrire_aun_cours

        """
        pass

    def test_inscriptions_cours(self):
        """Test case for inscriptions_cours

        """
        pass

    def test_inscrire_aun_cours(self):
        """Test case for inscrire_aun_cours

        """
        pass

    def test_prerequis_non_acquis(self):
        """Test case for prerequis_non_acquis

        """
        pass


if __name__ == '__main__':
    unittest.main()
