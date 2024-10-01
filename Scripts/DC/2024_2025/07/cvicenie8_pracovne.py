# jednoduchá hra s hádzaním kocky nazvaná "Krok za krokom":

# Pravidlá hry:
# Začiatočná pozícia: Hráč začína na pozícii 0.
# Cieľ: Cieľom je dosiahnuť pozíciu 30.
# Pohyb: V každom kole hráč hodí šesťstrannou kockou:
# Hod 1 alebo 2: posunie sa o 1 krok dozadu (nikdy však nižšie než pozícia 0).
# Hod 3, 4 alebo 5: posunie sa o 1 krok dopredu.
# Hod 6: hodí kockou znova a posunie sa o počet bodov, ktorý padol v druhom hode.
# Koniec hry: Hra končí, keď hráč dosiahne pozíciu 30.

import random

def hod_kockou():
    vyselok = random.randint(1, 6)
    return vyselok

aktualna_pozicia = 0
koniec = 30

while aktualna_pozicia < koniec:
    vysledok_hodu = hod_kockou()
    if vysledok_hodu == 1 or vysledok_hodu == 2:
        aktualna_pozicia = aktualna_pozicia - 1
    elif vysledok_hodu == 3 or vysledok_hodu == 4 or vysledok_hodu == 5:
        aktualna_pozicia = aktualna_pozicia + 1
    elif vysledok_hodu == 6:
        vysledok_hodu = hod_kockou()
        
    print("Hráč hodil ", vysledok_hodu, " a je na pozícii ", aktualna_pozicia)
    
        
