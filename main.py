# Definició de classes
# Autors Adrià Boix i Clàudia Fariña Fernandez
class UnitatFormativa:
    nom = None

    def __init__(self, nom):
        self.nom = nom


# Inici del programa
uf1 = UnitatFormativa("UF1. Desenvolupament del programari")
uf2 = UnitatFormativa("UF2. Optimització del programari")
uf3 = UnitatFormativa("UF3. Introducció al Disseny Orientat a Objectes")

print(uf1.nom)
print(uf2.nom)
print(uf3.nom)
