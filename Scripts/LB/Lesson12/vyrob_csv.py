# Vikinka
# 5 dec 2023
# program na vypisanie hodnot gaussianu a jeho derivaciew do suboru csv

import math as m
import pandas as pd 

# funkcia na vypocet hodnoty gaussianu
def get_f(x):
    N = 0.5
    alfa = 2.0
    x0 = 5.0
    y = N*m.exp(-alfa*(x-x0)**2)
    return y

# vypocet numerickej derivacie funkcie get_f
def get_df(x):
    dx = 1.0e-4
    f1 = get_f(x-dx)
    f2 = get_f(x+dx)
    df = (f2-f1)/(2*dx)
    return df

def main():
    start = 0
    stop = 10.0 # 10 lebo mame stred v bode 5 tak nech to je symetricke
    steps = 15 # na 15 miestach pocitame hodnotu funkcie

    # vypocet hodnot
    # definicia praydnzch listov
    xs = []
    ys = []
    dys = []

    x = start

    # definovanie velkosti kroku
    dx = (stop-start)/steps

    for i in range(steps):
       x = x+dx
       y = get_f(x)
       dy = get_df(x)
       xs.append(x)
       ys.append(y)
       dys.append(dy)

    # zhrnutie a uprava data pre import do pandas(dataframe)
    data = {
            "x": xs,
            "y": ys,
            "dy": dys
            }

    # vytvorenie datoveho typu dataframe pomocou pandas
    # dataframe umoznuje pracu s datami a ich import/export
    dataframe_data = pd.DataFrame(data)

    dataframe_data.to_csv("data.csv", sep = ";", index = False, float_format = pd.set_eng_float_format(accuracy=4)) #ulozime to do suboru s nazvom data.csv, sep znamena separacia dat v stlpcoch a zvolili sme si na to bodkociarku

if __name__=="__main__":
    main()
