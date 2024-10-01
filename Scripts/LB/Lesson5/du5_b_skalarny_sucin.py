# program na vypocet skalarneho sucinu dvoch vektorov? Neviem, nepochopila som zadanie domacej ulohy
# Viki Stefancova
# 23 oct 2023

vektor_1_1 = input("Zadaj suradnicu 1 vektora c_i: ")
vektor_1_2 = input("Zadaj suradnicu 2 vektora c_i: ")
vektor_1_3 = input("Zadaj suradnicu 3 vektora c_i: ")
vektor_1_4 = input("Zadaj suradnicu 4 vektora c_i: ")
vektor_1_5 = input("Zadaj suradnicu 5 vektora c_i: ")
vektor_1_6 = input("Zadaj suradnicu 6 vektora c_i: ")

vektor_2_1 = input("Zadaj suradnicu 1 vektora c_j: ")
vektor_2_2 = input("Zadaj suradnicu 2 vektora c_j: ")
vektor_2_3 = input("Zadaj suradnicu 3 vektora c_j: ")
vektor_2_4 = input("Zadaj suradnicu 4 vektora c_j: ")
vektor_2_5 = input("Zadaj suradnicu 5 vektora c_j: ")
vektor_2_6 = input("Zadaj suradnicu 6 vektora c_j: ")


# definicia datoveho typu list
c_i = [float(vektor_1_1), float(vektor_1_2), float(vektor_1_3), float(vektor_1_4), float(vektor_1_5), float(vektor_1_6)]
c_j = [float(vektor_2_1), float(vektor_2_2), float(vektor_2_3), float(vektor_2_4), float(vektor_2_5), float(vektor_2_6)]
print("c_i = ",c_i)
print("c_j = ",c_j)
print()

vysledok = [x*y for x,y in zip(c_i,c_j)]
print("skalarny sucin medzi vektormi c_i a c_j je ",sum(vysledok))
print()




# ukazane na hodine

#definicia vektorov
ci = [1,2,3,3,2,1]
cj = [2,2,2,1,1,1]

#vypis zadanych vektorov a ich dlzky/dimenzie
print("vektor ci je: ",ci)
print("pocet clenov ci je: ",len(ci))

print("vektor cj je: ",cj)
print("pocet clenov cj je: ",len(cj))
print()

# old skuul vypocet skalarneho sucinu
sum=0
for i,j in zip(ci,cj):
    print(i,j,i*j)
    sum+=i*j
print("vysledok skalarneho sucinu: ",sum)

print()

#old skuul vypocet skalarneho sucinu s indexovanim polii
sum=0
for i in range(len(ci)):
    print(i) # vypise od 0 po dlzku ci - 0 az 5
    print(i,ci[i],cj[i])
    sum+=ci[i]*cj[i]
print("vysledok: ",sum)


