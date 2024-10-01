# Viki Stefancova
# 31 oct 2023
# program na list comprehension - make a list out of a list in a single line including a condition

# vyrobime si list a vypiseme
cars = ["Ford", "Kia", "BMcQ", "BMW","Hiundai","Skoda","Volvo"]
print(cars)
print()

# vypis cez list comprehension
print ([car for car in cars])
print()


# vypisanie iba tych aut ktore maju male pismenko "a" v mene

#         3   1              2
acars = [car for car in cars if "a" in car]
print (acars)
print()


# vymenime nieco "BMW" za "Ziguli" 

#       3   2                              1
print([car if car != "BMW" else "Ziguli"  for car in cars])


# zamena vsetkych poloziek za to iste
print (["Hello!" for car in cars])

