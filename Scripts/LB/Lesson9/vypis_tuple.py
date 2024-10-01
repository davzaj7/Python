# Viki Stefancova
# 14 nov 2023
# pouzitie funkcie s argumentom tuple

def vypis_s_tuple(*ovocie):  # * = vsetky argumenty vo funkcii spoji do jedneho tuple s nazvom ovocie

    print(type(ovocie))

    for o in ovocie:
        print(" v argumentoch bolo: ",o)

print("zaciatok programu")
vypis_s_tuple("epl","hruska","marhula","3")






