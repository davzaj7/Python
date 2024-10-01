# jednoduchz while cyklus s podmienkou if a prikazmi break a continue
# Viki Stefancova
# 17 oct 2023

n_str = input("Zadaj pocet opakovani: ")

n = int(n_str)

#nastavenie pociatocnej hodnoty premennej i
i = 0

while i<n : #podmienka while cyklu
    if i==3:
        print("Ta daaaa")
    print(i, "je mensie ako ",n) #prvy prikaz
    i+=1 # druhy prikaz i = i+1

print("i je: ",i)
print("hotovo")
print()



#druha cast kodu s break
#nastavenie pociatocnej hodnoty premennej i
i = 0

while i<n : #podmienka while cyklu
    if i==3:
        print("Ta daaaa")
        break #tento prikaz zlomi alebo ukonci czklus a vykona prikazy za cyklom
    print(i, "je mensie ako ",n) #prvy prikaz
    i+=1 #druhy prikaz i=i+1

print("i je: ",i)
print("hotovo")
print()


#tretia cast kodu s continue
#nastavenie pociatocnej hodnoty premennej i
i = 0

while i<n : #podmienka while cyklu
    i+=1 # prvy prikaz i=i+1
    if i==3:
        print("Ta daaaa")
        continue #tento prikaz preskoci kod az po koniec while a vrati sa spat na podmienku a pokracuje = takze preskoci trojku
    print(i, "je mensie ako ",n) #druhy prikaz

print("i je: ",i)
print("hotovo")
