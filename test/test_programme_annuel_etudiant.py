"""
    Course enrollments service

    A set of API endpoints that allow you to enroll students to courses  # noqa: E501

    The version of the OpenAPI document: 1.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_inscription_cours_sdk
from osis_inscription_cours_sdk.model.inscription_aun_cours import InscriptionAUnCours
from osis_inscription_cours_sdk.model.inscriptions_aun_partenariat import InscriptionsAUnPartenariat
from osis_inscription_cours_sdk.model.inscriptions_pour_une_mini_formation import InscriptionsPourUneMiniFormation
globals()['InscriptionAUnCours'] = InscriptionAUnCours
globals()['InscriptionsAUnPartenariat'] = InscriptionsAUnPartenariat
globals()['InscriptionsPourUneMiniFormation'] = InscriptionsPourUneMiniFormation
from osis_inscription_cours_sdk.model.programme_annuel_etudiant import ProgrammeAnnuelEtudiant


class TestProgrammeAnnuelEtudiant(unittest.TestCase):
    """ProgrammeAnnuelEtudiant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProgrammeAnnuelEtudiant(self):
        """Test ProgrammeAnnuelEtudiant"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProgrammeAnnuelEtudiant()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
