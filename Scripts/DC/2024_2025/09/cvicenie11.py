# Hra "Divný Janko" bola úspešne naprogramovaná v Pythone. 
# Hra začína s Jankom v bode 50, a jeho cieľom je dostať sa do školy, 
# ktorá je v bode 100. Každé ráno sa posúva o 10 
# bodov smerom k škole, až kým nedosiahne bod 50. 
# Odtiaľ si začne hádzať mincou: ak padne znak, posunie sa o 10 
# bodov dopredu, a ak padne rub, posunie sa o 10 bodov dozadu. 
# Janko sa nemôže vrátiť domov, takže najnižší bod, na ktorý môže klesnúť,
#  je 50. Hra pokračuje, až kým sa Janko nedostane do školy.

import random

def hod_mincou():
    vysledok = random.choice([1,2])
    if vysledok == 1:
        return 10
    if vysledok == 2:
        return -10

domov = 0
skola = 100
aktualna_poloha = 50
dni = ["pondelok", 'utorok', 'streda', 'štvrtok', 'piatok']

for i in range(5):
    while aktualna_poloha != domov and aktualna_poloha != skola:
        vysledok = hod_mincou()
        aktualna_poloha = aktualna_poloha + vysledok
        print('Aktualna poloha je: ', aktualna_poloha)

    if aktualna_poloha == domov:
        print('Janko je doma v ', dni[i])
    if aktualna_poloha == skola:
        print('Janko je v skole v ', dni[i])

    aktualna_poloha = 50
