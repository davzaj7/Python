# 1. scitaj cisla od 1 po 10

vysledok = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(vysledok)

vysledok = 0

for cislo in range(1, 11):
    vysledok = vysledok + cislo
    print(cislo, vysledok)

print(vysledok)

# 2. Vypis 7krat "Ahoj"

for i in range(7):
    print("Ahoj")

# 3. Vypis 7krat "Ahoj" a cislo opakovania

for i in range(7):
    print("Ahoj", i)

# 4. Vypis 7krat "Ahoj" a cislo opakovania, ale zacni od 1

for i in range(1, 8):
    print("Ahoj", i)

# 5. Vypis 7krat "Ahoj" a cislo opakovania, ale zacni od 1 a zvysuj o 2

for i in range(1, 8, 2):
    print("Ahoj", i)

# 6. podmienka if - iba parne cisla

for i in range(1, 8):
    if i % 2 == 0:
        print("Ahoj", i)

# 7. podmienka if - iba neparne cisla

for i in range(1, 8):
    if i % 2 == 1:
        print("Ahoj", i)

# 8. scitaj parne cisla od 1 po 10

vysledok = 0

for cislo in range(1, 11):
    if cislo % 2 == 0:
        vysledok = vysledok + cislo
        print(cislo, vysledok)

print(vysledok)