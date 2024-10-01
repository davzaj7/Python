# Viki Stefancova
# kvadraticna rocnice
# 10 oct 2023

import math

a_str = input("Vloz koeficient a : ")
a = float(a_str)
b_str = input("Vloz koeficient b : ")
b = float(b_str)
c_str = input("Vloz koeficient c : ")
c = float(c_str)

# vypocet determinantu
D = b**2-(4*a*c)

if D>0:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print("Riesenim rovnice su dva korene: ",x1," a ",x2)
elif D==0:
    x = -b/(2*a)
    print("Riesenim rovnice je koren: ",x)
else:
    print("Rovnica nema realny koren a tebe sa nechce riesit komplexne cisla")

