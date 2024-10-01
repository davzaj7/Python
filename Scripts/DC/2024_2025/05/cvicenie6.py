# 1. Jednoduchá kalkulačka
# Úloha: Napíšte funkcie pre sčítanie, odčítanie, násobenie a delenie, ktoré prijmú dva argumenty a vrátia výsledok.

# 2. Kontrola deliteľnosti
# Úloha: Napíšte funkciu, ktorá zistí, či je číslo deliteľné iným číslom. Funkcia by mala prijímať dve čísla a vrátiť True alebo False.

def je_parne(cislo):
    return cislo % 2 == 0

cislo1 = int(input("Zadaj cislo 1: "))
print('Cislo ', cislo1, ' je parne: ', je_parne(cislo1))

# 3. Konvertor teploty
# Úloha: Vytvorte funkciu, ktorá prevedie teplotu z Fahrenheitov na Celzia (a naopak). Funkcia by mala prijímať teplotu a typ konverzie ako argumenty.

def fahrenheit_na_celzia(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celzia_na_fahrenheit(celzia):
    return celzia * 9/5 + 32

teplota = int(input("Zadaj teplotu: "))
typ = input("Zadaj typ konverzie (fahrenheit/celzia): ")

if typ == 'fahrenheit':
    print('Teplota v stupnoch celzia: ', fahrenheit_na_celzia(teplota))
elif typ == 'celzia':
    print('Teplota v stupnoch fahrenheit: ', celzia_na_fahrenheit(teplota))
else:
    print('Neznamy typ konverzie')

# 4. Výpočet faktoriálu
# Úloha: Vytvorte funkciu na výpočet faktoriálu daného čísla. Faktoriál čísla n je definovaný ako n * (n-1) * (n-2) * ... * 1.

def faktorial(cislo):
    vysledok = 1
    for i in range(1, cislo + 1):
        vysledok = vysledok * i
    return vysledok

cislo = int(input("Zadaj cislo: "))
print('Faktorial cisla ', cislo, ' je ', faktorial(cislo))