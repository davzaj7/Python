# 1. while cycle
pocitadlo = 0

while pocitadlo < 10:
    print(pocitadlo)
    pocitadlo = pocitadlo + 1

print("Koniec programu")

# 2. cislo ako input

pocitadlo = 0
cislo = int(input("Zadaj cislo: "))


while pocitadlo <= cislo:
    print(pocitadlo)
    pocitadlo = pocitadlo + 1

print("Koniec programu")

# 3. zadaj 2 cislana vstupe a vypis vsetky cisla od prveho cisla po druhe cislo

cislo1 = int(input("Zadaj cislo 1: "))
cislo2 = int(input("Zadaj cislo 2: "))

while cislo1 <= cislo2:
    print(cislo1)
    cislo1 = cislo1 + 1

print("Koniec programu")

# 4. priklad na if a elif

cislo = int(input("Zadaj cislo: "))

if cislo < 0:
    print("Cislo je zaporne")
elif cislo == 0:
    print("Cislo je nula")
else:
    print("Cislo je kladne")

print("Koniec programu")

# 5. zadaj meno

meno = input("Zadaj meno: ")

if meno == "Peter":
    print("Ahoj Peter")
elif meno == "Jozef":
    print("Ahoj Jozef")
elif meno == "Jana":
    print("Ahoj Jana")
else:
    print("Ahoj neznamy")

print("Koniec programu")

# 6. zadavaj mena kym nezadas "koniec"

while True:
    meno = input("Zadaj meno: ")
    if meno == "koniec":
        break
    else:
        print("Ahoj " + meno)

print("Koniec programu")

# 7. ak zadas neparne cislo tak vypis "neparne cislo" a skonci program

while True:
    cislo = int(input("Zadaj cislo: "))
    if cislo % 2 == 1:
        print("Neparne cislo")
        break
    else:
        print("Parne cislo")
