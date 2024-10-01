# Vikinka
# 21 nov 2023
# pocitanie rovnice f(x)=phi(x)-x iteracnou metodou
# f(x) = (x-1)*(x**2+1)

import math as m
def phi(x):
    return x*x*x-x**2+2*x-1

# hlavny program
def main():

    x0_input=input("zadajte odhad korena:  ")
    try:
        x0=float(x0_input)
        print()
    except ValueError:
        print("Program konci. Ty kraavo, nezadala si vstup kt. sa da konvertovat na float!!")

# iteraaciooon
    max_i=100000
    treshold=1E-8
    print("Maximalny pocet iteracii: ",max_i)
    print("presnost   :",treshold)
    print()

    for i in range(max_i):
        # x_n+1=phi(x_i) <=> x1 = phi(x0)
        x1=phi(x0)
        
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

