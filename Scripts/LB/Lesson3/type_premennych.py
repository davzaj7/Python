#viki Stefancova
#typy premennych v python a funkcia type()
#3 oct 2023

#def
a_str="14"
a_int=14
a_float=14.
a_complex=14+14j
a_bool=a_int>0

#vypis premennej a jej type()
print(a_str,type(a_str)) # str(14)
print(a_int,type(a_int)) # int(14)
print(a_float,type(a_float)) # float(14)
print(a_complex,type(a_complex)) # complex(14)
print(a_bool,type(a_bool)) # bool(14)

print()

# test bool(14)
print()
print(bool(14)) # ocakavame true
print(bool(00)) # ocakavame false

