# Viki Stefancova
# program na vypocet obvodu a obsahu stvorca alebo obdlznika
# 8 oct 2023

import math

def stvorec(a,b):
    print("a = "+str(a)+", b = "+str(b))
    O = 2*(a+b)
    S = a*b
    if a==b:
        print ("obvod stvorca je "+str(O)+" a obsah je "+str(S))
    else:
        print ("obvod obldznika je "+str(O)+" a obsah je "+str(S))

def kruh(r):
    print("r = "+str(r))
    O = 2*math.pi*r
    S = math.pi*r**2
    print("obvod kruhu je "+str(O)+" a obsah je "+str(S))

stvorec(2,2)
print()
stvorec(2,3)
print()
print()
kruh(3)


