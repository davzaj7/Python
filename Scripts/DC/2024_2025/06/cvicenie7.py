# Hra "Divný Janko" bola úspešne naprogramovaná v Pythone. Hra začína s Jankom v bode 50, a jeho cieľom je dostať sa do školy, 
# ktorá je v bode 100. Každé ráno sa posúva o 10 bodov smerom k škole, až kým nedosiahne bod 50. 
# Odtiaľ si začne hádzať mincou: ak padne znak, posunie sa o 10 bodov dopredu, a ak padne rub, posunie sa o 10 bodov dozadu. 
# Janko sa nemôže vrátiť domov, takže najnižší bod, na ktorý môže klesnúť, je 50. Hra pokračuje, až kým sa Janko nedostane do školy.








































import random

def hod_minca():
    hod = random.choice(["znak", "rub"])
    if hod == "znak":
        return 10
    elif hod == "rub":
        return -10

aktualna_poloha = 50
skola = 100
domov = 0
dni = ["pondelok", 'utorok', 'streda', 'štvrtok', 'piatok']
pocitadlo = 0

while pocitadlo < 5:
    while aktualna_poloha != skola and aktualna_poloha != domov:
        vysledok = hod_minca()
        # print("Posuvame sa o ", vysledok, " krokov")
        aktualna_poloha = aktualna_poloha + vysledok
        # print("Aktualna poloha je ", aktualna_poloha)
    if aktualna_poloha == skola:
        print("Janko je v škole v ", dni[pocitadlo])
    elif aktualna_poloha == domov:
        print("Janko je doma v ", dni[pocitadlo])
    pocitadlo = pocitadlo + 1
    aktualna_poloha = 50


































# import random

# # Začiatočná pozícia Janka
# pozicia = 50

# def hod_mincou():
#     hod = random.choice(["znak", "rub"])
#     if hod == "znak":
#         return 10
#     else:
#         return -10

# while pozicia != 100 and pozicia != 0:
#     print('Janko ide o 10 bodov a teraz je na pozícii 50')
#     vysledok = hod_mincou()
#     pozicia += vysledok
#     # Upravený výpis, aby vždy ukazoval priebežnú pozíciu
#     print(f"Janko ide o {vysledok} bodov a teraz je na pozícii {pozicia}")

# if pozicia == 100:
#     print("Janko sa dostal do školy")
# elif pozicia == 0:
#     print("Janko sa dostal domov")


