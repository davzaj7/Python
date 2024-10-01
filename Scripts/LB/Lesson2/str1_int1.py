#program na test prace s retazcom znakov name a celym cislom integer age
# autor: Viktoria Stefancova
#26.9.2023

#definicia\priradenie premennych name a age
name="Viktoria" #string
age=22 #integer

#overenie typu premennej cez funkciu type()
print(type(name))
print(type(age))

#vypis obsahu premennych name a age
print(name)
print(age)

#kombinovany vypis
print("name =",name)
print("age =",age)
print()

#vypis premennych name a age spolu
print(name,age)
print(name+" "+str(age))
print()

#dalsie moznosti kombinovaneho vypisu
print("{} is {} years old.".format(name,age))
print("{0} is {1} years old.".format(name,age))#name is 0 element and age is 1 element in the format sequence




