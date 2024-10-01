# program pomocou inputov vypocita obvod a obsah utvaru, ktory si vyberiem
# viki Stefancova
# 15 oct 2023

import math

vypocet_str = input("Chces pocitat: 1 - kruh, 2 - stvorec, 3 - obdlznik ")
v = float(vypocet_str)

if v==1:
    polomer_str = input("Zadaj polomer : ")
    r = float(polomer_str)
    O = 2*math.pi*r
    S = math.pi*r**2
    print("Obvod kruhu je: {:.3f}".format(O)+" a obsah je: {:.3f}".format(S))
elif v==2:
    strana_str = input("Zadaj dlzku strany : ")
    a = float(strana_str)
    O = 4*a
    S = a**2
    print("Obvod stvorca je "+str(O)+" a obsah je "+str(S))
elif v==3:
    strana_a_str = input("Zadaj dlzku strany a :")
    a = float(strana_a_str)
    strana_b_str = input("Zadaj dlzku strany b :")
    b = float(strana_b_str)
    O = 2*(a+b)
    S = a*b
    print("Obvod obdlznika je "+str(O)+" a obsah je "+str(S))
else:
    print("Mozes vybrat iba: 1 - kruh, 2 - stvorec, 3 - obdlznik")

