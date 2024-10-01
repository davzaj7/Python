# Viki
# program na obvod a obsah kruhu, stvorca a obdlzika ktory zevraj mame povazovat za semestralny projekt
# 19 nov 2023, edit 25.11.2023

import math

# definicia funkcii
def o_stvorec(a):
    return 4*a
def s_stvorec(a):
    return a**2
def o_obdlznik(a,b):
    return 2*(a+b)
def s_obdlznik(a,b):
    return a*b
def o_kruh(r):
    return 2*math.pi*r
def s_kruh(r):
    return math.pi*r**2

while(1):
    utvar = input("Dobry den, co by ste chceli vypocitat? Na vyber mame \"kruh\", \"stvorec\" a \"obdlznik\":  ")

    if utvar=="kruh":
        while(1):

            vypocet = input("Chcete pocitat \"obvod\" alebo \"obsah\"?  ")
            if vypocet=="obvod":
                r = input("Aky je polomer kruhu?  ")
                print("Obvod kruhu je:  {:.2f}".format(o_kruh(float(r))))
                break   

            elif vypocet=="obsah":
                r = input("Aky je polomer kruhu?  ")
                print("Obsah kruhu je:  {:.2f}".format(s_kruh(float(r))))
                break
            
            else:
                print("Taky vstup nepoznam, skuste znovu.")
        
        if input("Chcete pocitat nieco dalsie? (\"ano\" / \"nie\")  ")=="nie":
            exit()

    elif utvar=="stvorec":
        while(1):

            vypocet = input("Chcete pocitat \"obvod\" alebo \"obsah\"?  ")
            if vypocet=="obvod":
                a = input("Aka dlha je strana stvorca?  ")
                print("Obvod stvorca je:  {:.2f}".format(o_stvorec(float(a))))
                break   

            elif vypocet=="obsah":
                a = input("Aka dlha je strana stvorca?  ")
                print("Obsah stvorca je:  {:.2f}".format(s_stvorec(float(a))))
                break
            
            else:
                print("Taky vstup nepoznam, skuste znovu.")
        
        if input("Chcete pocitat nieco dalsie? (\"ano\" / \"nie\")  ")=="nie":
            exit()
        

    elif utvar=="obdlznik":
        while(1):

            vypocet = input("Chcete pocitat \"obvod\" alebo \"obsah\"?  ")
            if vypocet=="obvod":
                a = input("Aka dlha je prva strana obdlznika?  ")
                b = input("Aka dlha je druha strana obdlznika?  ")
                print("Obvod obdlznika je:  {:.2f}".format(o_obdlznik(float(a),float(b))))
                break   

            elif vypocet=="obsah":
                a = input("Aka dlha je prva strana obdlznika?  ")
                b = input("Aka dlha je druha strana obdlznika?  ")
                print("Obsah obdlznika je:  {:.2f}".format(s_obdlznik(float(a),float(b))))
                break
            
            else:
                print("Taky vstup nepoznam, skuste znovu.")
        
        if input("Chcete pocitat nieco dalsie? (\"ano\" / \"nie\")  ")=="nie":
            exit()
        
    else:
        print("Takyto utvar nepoznam, skuste znovu.")

