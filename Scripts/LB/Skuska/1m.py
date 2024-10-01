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
if type(ovocia) == list:
    print("ovocia je list") 
