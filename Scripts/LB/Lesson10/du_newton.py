# Vikinka
# 25 nov 2023
# pocitanie rovnice f(x)=0 Newtonovou metodou
# f(x) = (x-1)*(x**2+1)

import math as m
def get_x1(x):
    f=(x-1)*(x**2+1)
    df=3*x**2+1-2*x
    return x-f/df

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
        # x1 = x0 - f(x0)/(x0) lebo Newton
        x1=get_x1(x0)
        
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

