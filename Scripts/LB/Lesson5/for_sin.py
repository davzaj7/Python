# vypis hodnot funkcie sinus
# Viki Stefancova
# 17 oct 2023

import math

zaciatok=0
koniec=360

krok=int(input("Zadaj krok (v stupnoch): "))

for uhol in range(zaciatok,koniec,krok):
    uhol_v_rad=uhol*math.pi/180
    print(math.sin(uhol_v_rad))
