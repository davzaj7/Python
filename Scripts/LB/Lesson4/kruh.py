# Viki Stefancova
# obvod a obsah kruhu
# 10 oct 2023

import math

def kruh(r):
    O = 2*math.pi*r
    S = math.pi*r**2
    print("obvod kruhu je "+str(O)+" a obsah je "+str(S))

kruh(3)

print()

r=3
O = 2*math.pi*r
print("obvod je: {:.2f}".format(O))


