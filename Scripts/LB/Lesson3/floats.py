# Voiki Stefancova
#program na priklady prace s realnymi cislami (floats)
#3 oct 2023

#def prememnnych
a = 31.
b = 7.
print (" a = ",a)
print (" b = ",b)
print ()

#matematicke operacie s premennymi
c = a + b #scitanie
print (" a + b = ",c)

c = a - b #odcitanie
print (" a - b = ",c)

c = a * b #nasobenie
print (" a * b =",c)

c = a / b #delenie
print (" a / b = ",c)

c = a ** b #umocneniei na j
print (" a ** b = ",c, " Umocnenie **")

c = a // b #floor
print (" a // b = ",c, " Podiel bez zvysku")

c = a % b #modulo
print (" a % b = ",c," Zvysok po deleni")
print (" a % b = ",int(c)," Zvysok po deleni") #spravi z cecka integer - bez desatinneho miesta 
print()

# TIPS AND TRICS
a = a + a
print (a)
# ak po tomto budem pracovat s ickom, bude to uz nove i a teda 62

c = b

b = b + 1
print (b)
#podobne ako pri i, nove j uz je 8
b+=1
# skratewny zapis: j = j + 1. teraz uz bude j 9
print (b)
print (c) #k je hodnota j ktora bola posledna pred k takze 7






