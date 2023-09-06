
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.activites_aide_reussite_api import ActivitesAideReussiteApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_inscription_cours_sdk.api.activites_aide_reussite_api import ActivitesAideReussiteApi
from osis_inscription_cours_sdk.api.autorisation_api import AutorisationApi
from osis_inscription_cours_sdk.api.complement_de_formation_api import ComplementDeFormationApi
from osis_inscription_cours_sdk.api.contact_api import ContactApi
from osis_inscription_cours_sdk.api.cours_api import CoursApi
from osis_inscription_cours_sdk.api.demande_particuliere_api import DemandeParticuliereApi
from osis_inscription_cours_sdk.api.formulaire_api import FormulaireApi
from osis_inscription_cours_sdk.api.mini_formation_api import MiniFormationApi
from osis_inscription_cours_sdk.api.pae_valide_jury_api import PaeValideJuryApi
from osis_inscription_cours_sdk.api.periode_inscription_etudiant_api import PeriodeInscriptionEtudiantApi
from osis_inscription_cours_sdk.api.proposition_programme_api import PropositionProgrammeApi
