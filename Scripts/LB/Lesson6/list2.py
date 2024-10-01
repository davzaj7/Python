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

# je epl vo fruits?
if "epl" in fruits:
    print("ajfony tiez mame :P ")

# je cherry vo fruits?
if "cherry" in fruits:
    print("ceresanicky, ceresnicky, ceeeeresneeeeeee")
else:
    print("smutna ceresnicka nie je na zozname :( fnuk, pridana cez append ")
    fruits.append("cherry")

print(fruits)
print()

# zmena fruits pouzitim indexu
fruits[2]="pitahaya" # vymenime treti element, dlzka sa nemeni
print(fruits)
print(len(fruits))
print()

#vymazanie elementu 
fruits.remove("tralala")
print(fruits)
print(len(fruits))
print()

#vymazanie konkretneho elementu (e4 - index 3)
fruits.pop(3)
print(fruits)
print(len(fruits))
print()

#vycistenie listu fruits
fruits.clear()
print(fruits)
print(len(fruits))
print()

# znicenie = ja ho chcem znicit, ten list fruits
del fruits
print(fruits) # toto sa uz neda lebo je zniceny a premenna fruits neexistuje


