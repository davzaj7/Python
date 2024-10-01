# Viki Stefancova
# 31 oct 2023
# programcek na tuple --> ordered(index), UNCHANGABLE (=> rozdiel oproti listu), doplicates allowed

# def tuple (GULATE ZATVORKY!!!!!)
bordel = ("Volvo", 3.1, "TOM", 8 ,True, "apple", [1,2,3])
print(bordel)
print(type(bordel)) # vypis typu poloziek
print(len(bordel)) # vypis dlzky poloziek
print()

# kedze je tuple indexovane, mozeme si z nej vypisat polozky vypisat podla urciteho poradia
print(bordel[0]) # prvy element. index 0
print(bordel[1:4]) # druhy treti stvrty, index 1-3
print(bordel[-1]) #posledny element
print(bordel[-1][1]) # v poslednej polozke bordel vypise druhu polozku, index 1
print(bordel[0][-1]) # v prvej polozke bordel vypise posledne pismenko, index -1
print()
