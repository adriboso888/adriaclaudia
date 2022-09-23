# Definició de classes
from Modul_Professional import Modul_Professional
from UnitatFormativa import UnitatFormativa


def inicialitzar_modul_professional():
    global uf1, uf2, uf3, uf1
    # Inici del programa
    uf1 = UnitatFormativa("UF1. Desenvolupament del programari", 20)
    uf2 = UnitatFormativa("UF2. Optimització del programari", 20)
    uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes", 26)
    uf1.qualificacio = 8
    uf2.qualificacio = 10
    uf3.qualificacio = 4
    mp5 = Modul_Professional("MP05. Entorns de desenvolupament")
    mp5.afegir_Unitat_Formativa(uf1)
    mp5.afegir_Unitat_Formativa(uf2)
    mp5.afegir_Unitat_Formativa(uf3)


inicialitzar_modul_professional()


def mostrar_modul_professional():
    print(uf1.nom, ":", uf1.qualificacio)
    print(uf2.nom, ":", uf2.qualificacio)
    print(uf3.nom, ":", uf3.qualificacio)
    print(mp5.nom, ":", mp5.get_Qualificacio())


mostrar_modul_professional()