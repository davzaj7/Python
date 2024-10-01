# 1. vypiste cisla od 0 po 100, ktore su mensie ako 20 a vacsie ako 80
import random

mahodne = random.randint(0, 100)

for i in range(0, 101):
    if i < 20 or i > 80:
        print(i)

# zadas cislo na vstupe a vypis vsetky cisla od 0 po toto cislo

cislo = int(input("Zadaj cislo: "))

for i in range(0, cislo + 1):
    print(i)

# zadaj 2 cislana vstupe a vypis vsetky cisla od prveho cisla po druhe cislo

cislo1 = int(input("Zadaj cislo 1: "))
cislo2 = int(input("Zadaj cislo 2: "))

for i in range(cislo1, cislo2 + 1):
    print(i)

# 2. vypiste cisla od 0 po 100, ktore su delitelne 3 a zaroven 5

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


#  3. while cyklus - vypiste parnecisla od 0 po 100

i = 0

while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1


# 4. while cyklus - vypiste parnecisla od 0 po 100, ale zacnite od 1

i = 1

while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 1


# 5. while cyklus - vypiste parnecisla od 0 po 100, ale zacnite od 1 a zvysujte o 2

i = 1

while i <= 100:
    if i % 2 == 0:
        print(i)
    i = i + 2


# 6. while cyklus - vypiste parnecisla od 0 po 100, ale zacnite od 1 a zvysujte o 2, ale iba ak je cislo delitelne 3

i = 1

while i <= 100:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
    i = i + 2






