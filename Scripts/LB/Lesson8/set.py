# Viki Stefancova
# 7 nov 2023
# programcek na pracu s premennou set{} (mnozina)
    # set sa neda menit (da sa iba nieco pridat)
    # poradie je nahodne a vzdy ine pri kazdom printe
    # neindexovany

# set ako ovocie
fruit={"apple","banana","apple","cherry","orange"}
cfruit=fruit # cfruits je len pointer na fruit - akonahle zmenime fruit, zmenime aj cfruit (copy)
print(fruit)
print(type(fruit))
print(len(fruit))
print()

# vypis poloziek po jednej
for f in fruit:
    print(f)
print()

# pridanie polozky/dalsieho clena cez funkciu add
fruit.add("lichi")
print(fruit)
print(cfruit)
print()

# vymazanie polozky cez discard alebo remove
    # remove je silnejsi ale ak tam uz dopredu ta polozka nebola tak nefunguje
fruit.discard("apple")
fruit.discard("peach") # toto tu nie je ale pri discard to nevadi, pri remove by to vadilo
print(fruit)
print()

f="peach"
try:
    fruit.remove(f)
except:
    print("toto tam neni",f)
fruit.remove("apple")
print(fruit) # toto uz nepojde samo o sebe
print()


