# Viki Stefancova
# logicke operacie
# 10 oct 2023

velke = 10
male = 2

vstup = input("Zadaj cislo")

a = float(vstup)

podmienka1 = a<velke
podmienka2 = a>=male

print("Cislo je mensie ako ",velke," a sucasne vacsie alebo rovne ako ",male," : ",podmienka1 and podmienka2)

print("Cislo je mensie ako ",velke," alebo vacsie alebo rovne ako ",male," : ",podmienka1 or podmienka2)
