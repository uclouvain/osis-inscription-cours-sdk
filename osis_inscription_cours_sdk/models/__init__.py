# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_inscription_cours_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_inscription_cours_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_inscription_cours_sdk.model.autorise_inscrire_aux_cours import AutoriseInscrireAuxCours
from osis_inscription_cours_sdk.model.configuration_formulaire_inscription_cours import ConfigurationFormulaireInscriptionCours
from osis_inscription_cours_sdk.model.cours import Cours
from osis_inscription_cours_sdk.model.demande_particuliere import DemandeParticuliere
from osis_inscription_cours_sdk.model.effectuer_demande_particuliere import EffectuerDemandeParticuliere
from osis_inscription_cours_sdk.model.error import Error
from osis_inscription_cours_sdk.model.formulaire_inscription_cours import FormulaireInscriptionCours
from osis_inscription_cours_sdk.model.groupement import Groupement
from osis_inscription_cours_sdk.model.inline_response200 import InlineResponse200
from osis_inscription_cours_sdk.model.inscription_aun_cours import InscriptionAUnCours
from osis_inscription_cours_sdk.model.inscription_mini_formation import InscriptionMiniFormation
from osis_inscription_cours_sdk.model.inscriptions_pour_une_mini_formation import InscriptionsPourUneMiniFormation
from osis_inscription_cours_sdk.model.inscrire_aun_cours import InscrireAUnCours
from osis_inscription_cours_sdk.model.inscrire_a_une_mini_formation import InscrireAUneMiniFormation
from osis_inscription_cours_sdk.model.liste_mini_formations import ListeMiniFormations
from osis_inscription_cours_sdk.model.mini_formation import MiniFormation
from osis_inscription_cours_sdk.model.programme_annuel_etudiant import ProgrammeAnnuelEtudiant
