# Viktoria Stefancova
# 12 dec 2023
# Skuska (1o): Nacitajte vysku v stopach a palcoch a udajte vysledok v cm.

def prepocet_do_cm(stopy,palce):
    # prepocet podla vzorcov:
    cm_na_stopu = 30.48
    cm_na_palec = 2.54

    # vypocet celkovej dlzky
    celkovo_cm = stopy*cm_na_stopu+palce*cm_na_palec

    return celkovo_cm

def vklad_uzivatela():
    while True:
        try:
            stopy= float(input("Zadajte vysku v stopach: "))
            palce= float(input("zadajte vysku v palcoch: "))
            return stopy, palce
        except ValueError:
            print("Takyto vstup nepoznam. Prosim, zadajte vysku ako cislo.")

def main():

    while True:
        stopy, palce = vklad_uzivatela() # ocistene od nevhodnych inputov, lebo vyssie sme vyuzili Try-Except
        centimetre = prepocet_do_cm(stopy,palce) # finalny prepocet
        print("Zadali ste ",float(stopy)," stop a ",float(palce)," palcov.")
        print("V prepocte to je {:.2f}".format(float(centimetre))," centimetrov.")
        print()
        opacko = input("Chcete prepocitat dalsiu vysku? (Zadajte ano): ") # v pripade dalsich potrieb prepoctu
        if opacko != 'ano':
            break

if __name__ == "__main__":
    main()


# prepocet palcov na cm
# https://www.hackmath.net/sk/kalkulacka/premena-jednotiek-dlzky?unit1=inch&unit2=cm&dir=1#:~:text=Koeficientom%20premeny%20je%202.54%3B%20teda,alebo%20preme%C5%88te%20inch%20na%20cm.

# prepocet stop na cm
# https://www.hackmath.net/sk/kalkulacka/premena-jednotiek-dlzky?unit1=ft&unit2=cm&dir=1#:~:text=Koeficientom%20premeny%20je%2030.48%3B%20teda,120%20ft%20je%20ko%C4%BEko%20cm%3F
