# Viki Stefancova
# 24 oct 2023
# pouzivanie a moznosti premennej list

# definicia listu
fruits = [] # definicia prazdneho listu fruits
fruits = list() # rovnake ako o riadok vyssie
fruits = ["epl","wiki","telekom","tomejtou","piiich","tralala"]

# pocet elementov vo fruits:
Nfruits = len(fruits)
 
# vypis:
print(fruits)
print("pocet elementov: ",Nfruits)
print()

#
for fruit in fruits:
    print(fruit)
print()

for i,fruit in enumerate(fruits):
    print(i+1,fruit)
    print(i+1,fruit,fruits[i]) # to iste len inak
print()

# vypisy podla poradia elementu
print(fruits[0]) # vypise prvy element, index 0
print(fruits[1:3]) # vypise prvy elementy 2 az 3, indexy 1 az 2, lebo 3-1=2 :(
print(fruits[3:Nfruits]) # vypise elementy od 4 po posledny (vratane), index 3 az koniec
print(fruits[3:]) # podla Lukasa rovnake ako o riadok vyssie
print(fruits[-2]) # vypise predposledny element
print(fruits[Nfruits-2]) # to iste




