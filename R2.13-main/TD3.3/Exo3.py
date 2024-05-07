import math

# Variables
diametre_initial = 40  # en mm
diametre_final = 60  # en mm
largeur_lame = 36  # en mm
longueur_totale = 2400  # en mm
epaisseur_lame = 7.5  # en mm
variation_diametre = diametre_final - diametre_initial

# 1. Nombre de lames nécessaires pour le tablier en position fermée
nombre_lames = longueur_totale / largeur_lame

# 2. Longueur à enrouler
longueur_enrouler = nombre_lames * largeur_lame

# 3. Équation de la suite arithmétique du diamètre
def diametre_n(n):
    return diametre_initial + (n - 1) * variation_diametre

# 4. Circonférence parcourue pour le tour n
def circonference_n(n):
    return math.pi * diametre_n(n)

# 5. Longueur enroulée au tour n
def longueur_enroulee_n(n):
    return n * circonference_n(n)

# 6. Nouvelle longueur à enrouler
nouvelle_longueur_enrouler = longueur_enroulee_n(2)

# Affichage des résultats
print("Nombre de lames nécessaires :", nombre_lames)
print("Longueur à enrouler :", longueur_enrouler, "mm")
print("Nouvelle longueur à enrouler :", nouvelle_longueur_enrouler, "mm")
