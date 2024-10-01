#Autor: Viki Stefancova
#program vypise meno a vek
#3 oct 2023

#def premennych
name="Viki"
age=22

#jednoduchy vypis
print(name,age)
print()

#kombinaciaa vypisu s popisom
print("meno=",name)
print("vek",age)
print()

#vytvorenie vety z retazcov
veta=name+" is "+str(age)+" years old"
print(veta)
print()

#print s format
print("{0} is {1} years old.".format(name,age))
print()
print("{0:20} is {1:6d} years old.".format(name,age))
print()
print("{0:>20} is {1:<6d} years old.".format(name,age))
print()
