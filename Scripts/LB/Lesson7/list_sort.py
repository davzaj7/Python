# Viki Stefancova
# 31 oct 2023
# program na list sorting - zoradovanie 

# vyrobime si list a vypiseme
cars = ["Ford", "Kia", "BMcQ", "BMW","Hiundai","Skoda","Volvo"]
print(cars)
print()

# zoradenie cars podla abecedy
cars.sort()
print(cars)
print()

# tymto zistime v akom poradi su pismenka za sebou v pythone - zistili sme ze velke pismena su pred malymi
print("poradie pismenka W: ",ord("W"))
print("poradie pismenka c: ",ord("c"))
print()

# zoradenie tak ze c bude pred W:
# sort(key = str.lower) --> dame vsetko v sorte na male pismena
cars.sort(key = str.lower)
print(cars)
print()

# reverse zoradenie
cars.sort(reverse = True, key = str.lower)
print(cars)
print()


