# for cyklus s pouzitim datoveho typu list
# Viki Stefancova
# 17 oct 2023

#definicia datoveho typu list
ovocia = ["jablko","slivka","malina","v ziackej knizke",0.452]
farby = ["cervene","fjalova","rozpucena","5",""]

#jednoduchy for s listom - vypis
for o in ovocia: 
    print(o)

print("hotoffka")
print()


#for cyklus s listom a enumerate()
for i,o in enumerate(ovocia): #enumerate() priradi kazdej polozke v list nejake poradove cislo
    print("poradie: ",i," polozka: ",o)

print("hotovecko")
print()


#for cyklus s listom a zip()
for f,o in zip(farby,ovocia): #zip() spoji farby a ovocia - prve s prvym, druhe s druhym...
    print(f,o)

print("fujha uz sa mi fakt nesce")
