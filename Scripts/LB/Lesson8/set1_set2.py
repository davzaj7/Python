# Viki Stefancova
# 7 nov 2023
# praca s dvomi setmi

# definicia setov
fruits={"apple","banana","kiwi","cherry"}
softs={"apple","microsoft","amd"} # softs = softwares

print(fruits, len(fruits))
print(softs, len(softs))
print()

# spojenie (zjednotenie) dvoch setov: union
fs_union=fruits.union(softs)
print(fs_union, len(fs_union))
print()

# prienik dvoch setov: intersection
sf_intersection=fruits.intersection(softs)
print(sf_intersection,len(sf_intersection))
print()

# doplnok k prieniku dvoch setov (co sa neprekryva, neopakuje): symmetric_difference
fs_dif=fruits.symmetric_difference(softs)
print(fs_dif,len(fs_dif))
print()
