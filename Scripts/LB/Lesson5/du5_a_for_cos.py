# vypis hodnot funkcie sinus a kosinus
# Viki Stefancova
# 23 oct 2023

import math

zaciatok=0
koniec=360

krok=int(input("Zadaj krok (v stupnoch): "))

for uhol in range(zaciatok,koniec,krok):
    uhol_v_rad=uhol*math.pi/180
    print("pre uhol: {:.1f}".format(uhol_v_rad*180/math.pi),"stupnov, sin = {:.3f}".format(math.sin(uhol_v_rad)),", cos = {:.3f}".format(math.cos(uhol_v_rad)))
