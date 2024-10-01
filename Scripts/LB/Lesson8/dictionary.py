# Viki Stefancova
# 7 nov 2023
# programcek na pracu s dictionary - tiez nahodne vypisanie

# definicia dictionary (item is key:value) - {}, ma priradene ine vlastnosti ako set
car={
        "brand":"Ford",
        "model":"mustang",
        "year":1964
}

print(car)
print(type(car))
print()

# vypis napr "brand"
print(car["brand"])
# print(car[8]) # nebude fungovat lebo dictionary je unidexed
print(car.get("brand")) # to iste
print()
# car_keys_list=list(car_keys) # vyrobi list z car_keys

# ziskanie keys v premennej car
car_keys=car.keys()
print(car_keys)

# ziskanie values v premennej cars
car_values=car.values()
print(car_values)

# ziskanie items 
car_items=car.items()
print(car_items)

# zmena value pre dany key
car["year"]=2020
car.update({"year":2020}) # to iste ako o riadok vyssie
print(car)
print(car_values)

# pridanie items
car["color"]="black"
# car.update({"color":"black"}) # to iste ako o riadok vyssie
print(car)
print(car_keys)
print(car_values)

car["seats"]=4
print(car)
print(car_keys)
print(car_values)

# odobratie item z premennej car
car.pop("year")
del car["color"]
print(car)
print(car_keys)
print(car_values)

# vycistenie dictionary
car.clear()
print(car)

# vymazanie
del car
# print(car) vyhodi chybu, jedine ze try - except

