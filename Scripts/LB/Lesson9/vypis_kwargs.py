# Vikinka
# 14 nov 2023
# brutalne argumenty
# funkcia kwargs v argumente, dictionary v argumente

def vypis_kwargs(**kwargs): # ** = zmeni argumenty na dictionary, argiument musi vyzerat ako "meno=hodnota"

    print(type(kwargs))

    for nazov,hodnota in kwargs.items(): # kwargs sme itemami rozdelili na nazvy a hodnoty
        print("premenna {} ma hodnotu {}".format(nazov,hodnota)) # {} = dosadi premennu

print("zaciatok programu")

vypis_kwargs(meno="Miky", priezvisko="Makac", vek=3, mesto="Bratislava")









