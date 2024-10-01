# Vikinka
# 28 nov 2023
# vypocet pH slabej kyseliny

import math as m

def eval_H(x,KHA,c0):
    g=10.0**(-0.5115*x)

    a = g**2
    b= KHA
    c= -KHA*c0

    D = b**2-4*a*c

    x1 = (-b+m.sqrt(D))/(2*a)

    return x1

# hlavny program
def main():

    KHA = 1.752e-5
    c0 = 1e-4

    # odhad H
    x0=m.sqrt(c0+KHA)

    

# iteraaciooon
    max_i=100000
    treshold=1E-8
    print("Maximalny pocet iteracii: ",max_i)
    print("presnost   :",treshold)
    print()
    print("odhad [H+]:",x0)

    

    for i in range(max_i):
        # x_n+1=phi(x_i) <=> x1 = phi(x0)
        x1=eval_H(x0,KHA,c0)
        
        # vypis priebehu iteracie
        dif=abs(x1-x0)
        print(i,x0,x1,dif)

        # kontrola konvergencie |x1-x0|<treshold
        if dif < treshold:
            print("Konvergencia pre x= ",x1)
            break

        # x0=x1
        x0=x1

    # koniec main()
    return()

if __name__ == "__main__": # ked sa spusti program tak najskor pusti funkciu main()
    main()

