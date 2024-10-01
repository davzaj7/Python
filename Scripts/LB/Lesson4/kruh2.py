# Viki Stefancova
# obvod a obsah kruhu
# 10 oct 2023

import math

print()
r_str = input("Zadaj polomer kruhu: ")

try:
    r = float(r_str)
except:
    print("{} nie je cislo ".format(r_str))
    exit()


O = 2*math.pi*r
print("Obvod je: {:.3f}".format(O))


S = math.pi*r**2
print("obsah kruhu je: {:.5f}".format(S))

