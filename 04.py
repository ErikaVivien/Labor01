# szamologep



def adatkeres(tipus):
    szam = ""
    if tipus == "sz":
        szam = input("Kérem a számot: ")
        while not szam.isnumeric():
            print("Rossz érték!")
            szam = input("Kérem a számot: ")
        szam = int(szam)
    elif tipus == "n":
        pass
    return szam

print("Számológép")
szam1 = adatkeres("sz")

muvelet = input("Milyen művelet legyen (+, -, *, / )?: ")
while muvelet not in {"+", "-", "*", "/"}:
       print("Rossz műveleti jel!")
       muvelet = input("Milyen művelet legyen (+, -, *, / )?: ")

szam2 = adatkeres("sz")

eredmeny =0
if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2

print(str(szam1).rjust(50))
print(muvelet, end="")
print(str(szam2).rjust(49))
print("".rjust(50),"")
print(str(eredmeny).rjust(50))