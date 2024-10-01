# Vikinka
# 14 nov 2023
# funkcia ktora vyacia nejaku hodnotu

def vynasob5x(a):
    vysledok = a*5

    return vysledok # funkcia vrati iba jeden argument lebo sme viac nezadali

def spocitaj_odcitaj(a,b,c):

    sucet = a+b+c
    rozdiel = a-b-c

    return sucet,rozdiel # funkcia moze vratit viac ako jeden argument, musia byt oddelene ciarkami

print("zaciatok programu")
print(vynasob5x(10))
print(vynasob5x(2))
print("asi som pretiekla")

vysledok=vynasob5x(3) # do prenmennej vysledok ulozi vysledok z funkcie
c = vynasob5x(4) # do premennej c ulozi vysledok z funkcie
print("vysledky su ",vysledok,c)
print("uz fakt cikam")

coto = spocitaj_odcitaj(10,2,3) # priradi vysledok do coto

print(type(coto))
print(coto)
for ct in coto: # vypise po castiach
    print(ct)

print(coto[0]) # vypise prvu polozku z coto

print("ach jaj este 20 minut")










