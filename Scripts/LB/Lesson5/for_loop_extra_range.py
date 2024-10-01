# jednoduchy for cyklus 
# Viki Stefancova
# 17 oct 2023

n = int(input("vloz pocet opakovani: "))# nacitanie vstupu

#jednoduchy povodny for cyklus 
for i in range(n): #vytvori i a priradi mu hodnoty od 0 po n-1
    print("Hodnota i: ",i) # vypise i

print("hotoffka")
print()

#for cyklus so zaciatkom v dvojke miesto nuly
for i in range(2,n): #vytvori i a priradi mu hodnoty od 2 po n-1
    print("Hodnota i: ",i) # vypise i

print("hotoffka")
print()

#for cyklus so zaciatkom v 2 a krokom 3
for i in range(2,n,3): #vytvori i a priradi mu hodnoty od 2 po n-1 s krokom 3 (i sa zvacsuje o tri a nie o jedna)
    print("Hodnota i: ",i) # vypise i

print("hotoffka")
print()
