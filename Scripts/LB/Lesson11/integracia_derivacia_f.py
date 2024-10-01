# Vikinka
# numericka integracia a derivacia funkcie
# 28 nov 2023

def f(x):
    return x**2

def check_suma(a,b):
    return b**3/3-a**3/3

def main():

    # hranice integracie
    a=1
    b=3

    # derivacia pre:
    xx=2

    # pocet krokov
    n=10000
    dx=(b-a)/n

    suma=0.0

    # numericka integracia
    for i in range(n):

        x1=a+i*dx
        x2=x1+dx

        suma+=(f(x1)+f(x2))/2*dx

    print("vysledok numerickej integracie: ",suma)
    print("vysledok analyickej integracie: ",check_suma(a,b))
    print()

    # numericka derivacia
    print("vysledok numerickej derivacie v x= ",xx," je: ",(f(xx+dx)-f(xx))/dx)
    print("vysledok analytickej derivacie v x= ",xx," je: ",2*xx)





if __name__=="__main__":
    main()
