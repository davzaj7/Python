# Vikinka
# 5 dec 2023
# nakresli graf z hodnot v data.csv

import pandas as pd
import matplotlib.pyplot as plt # to co kresli grafy

def main():

    # nacitanie vstupneho suboru
    dataframe_subor = pd.read_csv("data.csv", sep = ";")

    # vyseknutie hodnot y dataframe a transpozicia hodnot aby sme stlpce mali v stlpcoch 
    hodnoty = dataframe_subor.values.transpose()

    x = hodnoty[0] # hodnoty x su v prvom stlpci v csv subore
    y = hodnoty[1] # analogicky pre druhy a treti stlpec
    dy = hodnoty[2]

    # zobrazenie dat
    plt.figure(figsize = (4,4))

    # zakreslenie dat
    plt.plot(x,y,"bo", label = "gaussian")  #b - modra, o - kruzky, label je legenda
    plt.plot(x,dy, "r*", label = "derivaacia") # r - cervena, miesto kruzkov budu hviezdicky

    # ulozenie grafu do suboru
    grafik_png = "data.png"
    plt.savefig(grafik_png, dpi = 300)
    plt.close()

if __name__=="__main__":
    main()
