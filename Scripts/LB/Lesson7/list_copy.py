# Viki Stefancova
# 31 oct 2023
# program na list copy - kopirovanie listu 

# vyrobime si list a vypiseme
cars = ["Ford", "Kia", "BMcQ", "BMW","Hiundai","Skoda","Volvo"]
cars2 = cars # cars2 je len ukazovatel na cars - zmena v cars je zmena v cars2
cars_copy = cars.copy()
print("cars = ",cars)
print("cars2 = ",cars2)
print("cars_copy = ", cars_copy)
print()

# nieco zmenim v cars
cars.append("Mazda") # pridanie Mazdy
cars.pop(1) # vymazeme druhy item, index 1

print("cars = ",cars)
print("cars2 = ",cars2)
print("cars_copy = ",cars_copy)
print()
