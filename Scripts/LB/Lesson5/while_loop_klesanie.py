# jednoduchz while cyklus klesavy
# Viki Stefancova
# 17 oct 2023

n_str = input("Zadaj pocet opakovani: ")

n = float(n_str)

while n>3 : #podmienka while cyklu
    print(n, "je vacsie ako ",n) #prvz prikaz
    n=n/2 # druhy prikaz

print("n je: {:.1f}".format(n))
print("hotovo")
