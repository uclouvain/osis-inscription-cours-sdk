"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.9
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.api.proposition_programme_api import PropositionProgrammeApi  # noqa: E501


class TestPropositionProgrammeApi(unittest.TestCase):
    """PropositionProgrammeApi unit test stubs"""

    def setUp(self):
        self.api = PropositionProgrammeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_soumettre_proposition_programme(self):
        """Test case for soumettre_proposition_programme

        """
        pass


if __name__ == '__main__':
    unittest.main()
