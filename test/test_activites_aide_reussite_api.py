"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.8
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api.activites_aide_reussite_api import ActivitesAideReussiteApi  # noqa: E501


class TestActivitesAideReussiteApi(unittest.TestCase):
    """ActivitesAideReussiteApi unit test stubs"""

    def setUp(self):
        self.api = ActivitesAideReussiteApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_activites_aide_reussite(self):
        """Test case for get_activites_aide_reussite

        """
        pass

    def test_post_activites_aide_reussite(self):
        """Test case for post_activites_aide_reussite

        """
        pass

    def test_post_completer_inscription_par_activites_aide_reussite(self):
        """Test case for post_completer_inscription_par_activites_aide_reussite

        """
        pass

    def test_post_ne_pas_completer_inscription_par_activites_aide_reussite(self):
        """Test case for post_ne_pas_completer_inscription_par_activites_aide_reussite

        """
        pass


if __name__ == '__main__':
    unittest.main()
