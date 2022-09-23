from unittest import TestCase

from Modul_Professional import Modul_Professional
from UnitatFormativa import UnitatFormativa


class TestModulProfessional(TestCase):
    def test_get_qualificacio(self):
        mp = Modul_Professional("Prova de mòdul professional");
        uf1 = UnitatFormativa("UF1", 10);
        uf1.qualificacio = 0
        uf2 = UnitatFormativa("UF2", 40);
        uf2.qualificacio = 10
        mp.afegir_Unitat_Formativa(uf1)
        mp.afegir_Unitat_Formativa(uf2)
        assert(mp.get_Qualificacio() == 8)
