# 1. Jednoduchá kalkulačka
# Úloha: Napíšte funkcie pre sčítanie, odčítanie, násobenie a delenie, ktoré prijmú dva argumenty a vrátia výsledok.

def sucet(cislo1, cislo2):
    return cislo1 + cislo2

def rozdiel(cislo1, cislo2):
    return cislo1 - cislo2

def sucin(cislo1, cislo2):
    return cislo1 * cislo2

def podiel(cislo1, cislo2):
    return cislo1 / cislo2

cislo1 = int(input("Zadaj cislo 1: "))
cislo2 = int(input("Zadaj cislo 2: "))

print('Sucet: ', sucet(cislo1, cislo2))
print('Rozdiel: ', rozdiel(cislo1, cislo2))
print('Sucin: ', sucin(cislo1, cislo2))
print('Podiel: ', podiel(cislo1, cislo2))

