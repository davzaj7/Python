# Príklad: Práca s Polem Čísel
# Máme pole čísel a chceme s ním vykonať nasledujúce operácie:

# Vytvorte pole.
# Pridajte nové čísla do poľa.
# Vyhľadajte a vypíšte pozíciu (index) špecifického čísla.
# Usporiadajte pole od najmenšieho po najväčšie číslo.
# Vypočítajte a vypíšte priemernú hodnotu všetkých čísel v poli.
# Vypíšte čísla z poľa, ktoré sú nadpriemerné.


















# # 1. Vytvorenie poľa čísel
# cisla = [7, 12, 5, 3, 9]

# # 2. Pridanie nových čísel
# cisla.extend([4, 8])

# # 3. Vyhľadanie a vypísanie indexu špecifického čísla
# specificka_hodnota = 9
# if specificka_hodnota in cisla:
#     index = cisla.index(specificka_hodnota)
#     print(f"Číslo {specificka_hodnota} je na pozícii (indexe) {index} v poli.")
# else:
#     print(f"Číslo {specificka_hodnota} nie je v poli.")

# # 4. Usporiadanie poľa
# cisla.sort()
# print("Usporiadané pole:", cisla)

# # 5. Výpočet priemernej hodnoty
# priemer = sum(cisla) / len(cisla)
# print("Priemerná hodnota v poli:", priemer)

# # 6. Výpis nadpriemerných čísel
# print("Čísla nad priemerom:")
# for cislo in cisla:
#     if cislo > priemer:
#         print(cislo)



################### 2. cast #####################
# Zadanie:
# Máte pole čísel a vašou úlohou je nájsť najväčšie (maximálne) a najmenšie (minimálne) číslo v tomto poli.

# Príklad:
# Pole čísel: [3, 7, 2, 8, 4, 1]
# Výsledok:
# Maximálne číslo: 8
# Minimálne číslo: 1


# def najdi_max_min(cisla):
#     maximum = cisla[0]
#     minimum = cisla[0]
#     for cislo in cisla:
#         if cislo > maximum:
#             maximum = cislo
#         elif cislo < minimum:
#             minimum = cislo
#     return maximum, minimum

# # Testovanie funkcie
# cisla = [3, 7, 2, 8, 4, 1]
# max_cislo, min_cislo = najdi_max_min(cisla)
# print(f"Maximálne číslo: {max_cislo}")
# print(f"Minimálne číslo: {min_cislo}")
