# Viki Stefancova
# 30 oct 2023
# vycistenie bordelu v poli

import random

# definicia listu
fruits = ["epl",13,"wiki","telekom","","tomejtou","piiich",2,"tralala"]
print(fruits)
print()

# pokus ejkejej priatel sa cinil
for i in range(1000): # 1000x zopakuje pre kazdy prvok
    nahodne_cislo=random.randrange(1,10) # kazdemu prvku vyberie random cislo od 1 do 10
    if nahodne_cislo<3:  # pokial je random cislo mensie ako 3 tak to cislo prepise na prazdnu medzeru, zvysne cisla (3 a viac) necha ako su
        fruits.append("")
    fruits.append(nahodne_cislo) # prida 1000 prvkov k listu
random.shuffle(fruits) # zamiesa vsetky prvky vratane fruits do random poradia
print (fruits)
print()

for f in fruits:
    if isinstance (f, str) and len (f)>0:
        print (f)  # vypise vsetky slova (stringy) ktore maju viac ako nula znakov (takze sa zbavime aj medzier)
        




