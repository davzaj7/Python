# Vikinka
# 14 nov 2023
# slusne usporiadanie volania funkcii a organizacia programu

def zavolaj_kuriatko():

    print("kuratenko")

def zavolaj_kuriatka(n):

    for i in range(n):
        print("Kuratenka moje")

def zavolaj_kuriatka_farba(n, farba="zlte"):

    for i in range(n):
        print("{} kuriatko".format(farba))

def main(): # main = hlavna funkcia v programe ktora vola ostatne funkcie a je to prva funkcia ktora sa spusti v programe
    print("in the benninging")

    zavolaj_kuriatko()
    zavolaj_kuriatka_farba(3)

    print("KOHEU")

# vytvorime specialny magicky riadok aby vedel cim zacat
if __name__ == "__main__": # ked sa spusti program tak najskor pusti funkciu main()
    main()



