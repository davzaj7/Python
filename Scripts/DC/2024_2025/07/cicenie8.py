# jednoduchá hra s hádzaním kocky nazvaná "Krok za krokom":

# Pravidlá hry:
# Začiatočná pozícia: Hráč začína na pozícii 0.
# Cieľ: Cieľom je dosiahnuť pozíciu 30.
# Pohyb: V každom kole hráč hodí šesťstrannou kockou:
# Hod 1 alebo 2: posunie sa o 1 krok dozadu (nikdy však nižšie než pozícia 0).
# Hod 3, 4 alebo 5: posunie sa o 1 krok dopredu.
# Hod 6: hodí kockou znova a posunie sa o počet bodov, ktorý padol v druhom hode.
# Koniec hry: Hra končí, keď hráč dosiahne alebo prekročí pozíciu 30.




























import random

def hod_kockou():
    return random.randint(1, 6)

# Začiatočná pozícia hráča
pozicia = 0

while pozicia < 30:
    hod = hod_kockou()
    if hod <= 2:
        pozicia = max(0, pozicia - 1)
    elif hod <= 5:
        pozicia += 1
    else:
        pozicia += hod_kockou()
    print(f"Hráč hodil {hod}, teraz je na pozícii {pozicia}")

print("Hráč dosiahol cieľ!")
