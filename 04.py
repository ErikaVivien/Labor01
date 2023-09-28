# szamologep

print("Számológép")

szam1 = input("Kérem az első számot: ")
while not szam1.isnumeric():
    print("Rossz érték!")
    szam1 = input("Kérem az első számot: ")
szam1 = int(szam1)
muvelet = input("Milyen művelet legyen (+, -, *, /)?: ")
while muvelet not in {"+", "-", "*", "/"}:
       print("Rossz műveleti jel!")
       muvelet = input("Milyen művelet legyen (+, -, *, /)?: ")

szam2 = input("Kérem a második számot: ")
while not szam2.isnumeric():
    print("Rossz érték!")
    szam2 = input("Kérem a második számot: ")
szam2 = int(szam2)

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
print("".rjust(50),"_")
print(str(eredmeny).rjust(50))