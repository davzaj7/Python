# Viktoria Stefancova
# 12 dec 2023
# Skuska (1m): Napiste program, ktory otestuje, ci je dana premenna list, tuple alebo set.


# Vytvorim si premenne na kontrolu
ovocia = ["jablko","hruska","kiwi","baban","cucoriedka","slivka","marhula"]
auta = ("Audi", "Ford", "Skoda", "Porsche", "BMW", "Mercedes")
fyzikalnici = {"Viki", "Ondro", "Sonny", "Martin", "Lucka", "Veronika"}

print(ovocia)
print(auta)
print(fyzikalnici)

print()

print("Premenna ovocia je: ",type(ovocia))
print("Premenna auta je: ",type(auta))
print("premenna fyzikalnici je: ",type(fyzikalnici))

print()

def print_typ_premennej(premenna, meno_premennej):
    print(f"{meno_premennej} is a {type(premenna).__name__}")

# Typy premennej
print_typ_premennej(ovocia, "ovocia")
print_typ_premennej(auta, "auta")
print_typ_premennej(fyzikalnici, "fyzikalnici")
