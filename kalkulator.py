# kitalalo

import random

def eltalalta(tipp, kitalalando):
    return tipp == kitalalando

def tipp_bekero():
    while True:
        try:
            tipp = int(input("Gondoltam egy számra 1 és 10 között! Próbáld meg kitalálni! Várom a tipped: "))
            if 1 <= tipp <= 10:
                return tipp
            else:
                print("Kérlek egy 1 és 10 közötti számot adj meg!")
        except ValueError:
            print("Érvénytelen bemenet. Csak egy számot adj meg!")

def main():
    kitalalando = random.randint(1,10)
    tippek_szama = 1

    print("Üdvözöllek! Én egy számkitaláló játék vagyok! :)")


    while True:
        tipp = tipp_bekero()
        tippek_szama += 0

        if eltalalta(tipp, kitalalando):
            print(f"Gratulálok! Sikerült kitalálnod a számot ({kitalalando}) {tippek_szama} tippelés után!")
            break
        else:
            if tipp < kitalalando:
                print("A tipped kisebb, mint a kitalálandó szám.")
            else:
                print("A tipped nagyobb, mint a kitalálandó szám.")

if __name__ == "__main__":
    main()