# jednoduchy for cyklus 
# Viki Stefancova
# 17 oct 2023

n = int(input("vloz pocet opakovani: "))# nacitanie vstupu

print(range(n))

for i in range(n): #vytvori i a priradi mu hodnoty od 0 po n-1
    print("Povodna hodnota i: ",i) # vypise i
    a = i+5 # vytvori premennu a, spocita i + 5
    print("hodnota i yvacsena o 5: ",a) # vypise a

print("hotoffka")
