# Vikinka
# 5 dec 2023
# program na riesenie vlastneho problemu

import numpy as np
import pandas as pd

matica = pd.read_csv("matica.dat", sep=" ", header=None) # nacitanie v dataframe

F = matica.values

# vypocet vlastnych hodnot a vektorov

vl_cisla, vl_vektory = np.linalg.eig(F)

# zoradenie  vlastnych hodnoty a vektorov
print(vl_cisla)
zoradenie = vl_cisla.argsort() # vrati nam to hodnoty zoradenych indexov aby boli hodnoty zoradene od najmensich po najvacsie
print(vl_cisla[zoradenie])

vl_cisla = vl_cisla[zoradenie]
vl_vektory = vl_vektory[:,zoradenie] # prvy index = suradnice vektora, druhy index = poradie vektora

# vypis na obrazovku
for i, vl_cislo in enumerate(vl_cisla):
    print(i, vl_cislo)
    print(i, vl_vektory[:,i])


