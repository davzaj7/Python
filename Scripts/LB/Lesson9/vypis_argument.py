# Viki Stefancova
# 14 oct 2023
# zoznamka s funkciou, ziaden argument, zakladne pouzitie argumentu

def vypis_ziaden_argument():

    for i in range(3):
         print("Nic v argumente")

print("zaciatok programu")


def vypis_s_argumentom(n):

    for i in range(n):
        print("v argumente je: ",n)


a = 2
b = 3
print (a+b)
# vypis_ziaden_argument(2) # teraz sme netrafili pocet argumentov a funkcia nebude fungovat
vypis_ziaden_argument()


print("hotoffka")
vypis_s_argumentom(4)














