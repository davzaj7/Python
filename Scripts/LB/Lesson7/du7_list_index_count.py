# Viki Stefancova
# 31 oct 2023
# program na list index a count 

# vyrobime si list a vypiseme
cars = ["Ford", "Kia", "BMcQ", "BMW","Hiundai","Skoda","Volvo","Ford","BMW"]
print(cars)
print()

# za pomoci count() zistime pocet vyskytov napr. Ford a Kia
count = cars.count("Ford")
count2 = cars.count("Kia")
print("Pocet vyskytu Ford je: ",count)
print("Pocet vyskytu Kia je: ",count2)
print()

# za pomoci index() najdeme prvy vyskyt item s hodnotou Skoda
index = cars.index("Skoda")
print("Prvy vyskyt SIMPLY CLEVER je na indexe: ",index)

