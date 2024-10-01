# 1. Jednoduchá kalkulačka
# Úloha: Napíšte funkcie pre sčítanie, odčítanie, násobenie a delenie, ktoré prijmú dva argumenty a vrátia výsledok.

# funckie pre rozdiel
def rozdiel(a, b):
    vysledok = a - b
    return vysledok


cislo1 = int(input("Zadaj cislo 1: "))
cislo2 = int(input("Zadaj cislo 2: "))
cislo3 = int(input("Zadaj cislo 3: "))

moj_vysledok = rozdiel(cislo1, cislo2)
print(moj_vysledok)

# funkcia ktora vynasobi 3 cisla
def sucin(a,b,c):
    return a*b*c
    
vyslok_sucinu = sucin(cislo1,cislo2,cislo3)
print(vyslok_sucinu)

# ci je cislo parne
def je_parne(cislo):
    if cislo % 2 == 0:
        print("Cislo je parne")
    else:
        print("Cislo je neparne")
    
je_parne(cislo1)

def pozdrav(a):
    print("Ahoj " + a)

meno = input('Zadaj meno: ') 
pozdrav(meno)


# 2. Kontrola deliteľnosti
# Úloha: Napíšte funkciu, ktorá zistí, či je číslo deliteľné iným číslom. Funkcia by mala prijímať dve čísla a vrátiť True alebo False.


# 3. Konvertor teploty
# Úloha: Vytvorte funkciu, ktorá prevedie teplotu z Fahrenheitov na Celzia (a naopak). Funkcia by mala prijímať teplotu a typ konverzie ako argumenty.

# 4. Výpočet faktoriálu
# Úloha: Vytvorte funkciu na výpočet faktoriálu daného čísla. Faktoriál čísla n je definovaný ako n * (n-1) * (n-2) * ... * 1.