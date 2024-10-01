# Vikinka
# 14 nov 2023
# funkcia s predvolenymi hodnotami

def vypis_s_predvolenymi_hodnotami(oznam,n=3):# to su dva argumenty, keby bolo iba n bez =3 tak by sme to museli definovat ale takto je defaultne rovne 3
    for i in range(n):
        print(oznam)

def vypis_clovek(meno, priezvisko="Stefancova", vek=22):
    print("volam sa {meno} {priezvisko} a ma {vek} rokov ". format(meno=meno, priezvisko=priezvisko, vek=vek)) # vytvorili sme novu premennu meno ktorej priradim hodnotu meno z funkcie atd


print("zaciatok programu")
vypis_s_predvolenymi_hodnotami("fujha treba mi cikat",20) # zmenili sme n na 20 takze opakuje to 20x
print("fakt sa mi tu nechce byt")
vypis_s_predvolenymi_hodnotami("tato hodina trva nekonecne dlho") # 3x povie co chcem, lebo n=3 defaultne
print("stale nieco")
vypis_s_predvolenymi_hodnotami("fujha",n=4) # priame priradenie hodnoty do n, vyhodne to je ked je vela predvolenych a nechce sa nam to pamatat ich poradie
print("ble")
vypis_clovek("Vikinka") # pouzije obe predvolene
vypis_clovek("Miki",vek=3,priezvisko="Bucinsky") # pouzije vsetky hodnoty a nezalezi na poradi v akom sa zadaju
print("grcam")
vypis_clovek(meno="Jozo",vek=44) # prepise zadane a ostatne pouzije predvolene
print("uz nevladzem")

n=10
print("je tu ",n)
vypis_s_predvolenymi_hodnotami("co to spravi?") # premenna v programe sa nepobije s n vo funkcii, bude ignorovana dokedy to nezmenim, n v programe a n vo funkcii su ine premenne





