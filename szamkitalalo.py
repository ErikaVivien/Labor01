import tkinter as tk
from tkinter import simpledialog
import random

class Szamkitalalo:
    def __init__(self, root):
        self.root = root
        self.kitalalando_szam = random.randint(1, 10)
        self.tippek_szama = 0
        self.osszes_jatekos = []  # lista létrehozása a játékosok nevével és próbálkozások számával

        # megjelenés
        self.label_jatek = tk.Label(root, text="Üdvözöllek a szám kitaláló játékban!\nGondoltam egy számra 1 és 10 között!", font=("Arial", 12))
        self.label_jatek.pack(pady=20)

        self.tipp_be = tk.Entry(root, font=("Arial", 12))
        self.tipp_be.pack()

        self.tipp_gomb = tk.Button(root, text="Tippelés", command=self.tippellenorzo, font=("Arial", 12))
        self.tipp_gomb.pack()

        self.label_eredmeny = tk.Label(root, text="", font=("Arial", 12))
        self.label_eredmeny.pack()

    def tippellenorzo(self):
        tipp = self.tipp_be.get()
        self.tipp_be.delete(0, tk.END)

        if not tipp.isdigit():
            self.label_eredmeny.config(text="Kérlek, csak számot adj meg!", font=("Arial", 12))  # Hibaüzenet kiírása, ha nem számot adott meg a felhasználó
            return

        tipp = int(tipp)

        if not 1 <= tipp <= 10:
            self.label_eredmeny.config(text="A szám nem felel meg az intervallumnak.", font=("Arial", 12))  # Hibaüzenet kiírása, ha a szám nem 1 és 10 között van
            return

        self.tippek_szama += 1

        if tipp == self.kitalalando_szam:
            self.label_eredmeny.config(text=f"Gratulálok! Sikerült kitalálnod a számot ({self.kitalalando_szam}) {self.tippek_szama} tippelés után!", font=("Arial", 12))  # Üzenet kiírása, ha a játékos kitalálta a számot
            self.ranglista_felvetel()
            self.megjelenit_ranglistat()
            self.kitalalando_szam = random.randint(1, 10)  # Új véletlenszám generálása
            self.tippek_szama = 0  # Tipp számláló visszaállítása
            self.mentes_txt()  # Mentés TXT fájlba
        else:
            if tipp < self.kitalalando_szam:
                self.label_eredmeny.config(text="A tipped kisebb, próbáld meg nagyobbat!", font=("Arial", 12))  # Üzenet, ha a tipp kisebb, mint a kitalálandó szám
            else:
                self.label_eredmeny.config(text="A tipped nagyobb, próbáld meg kisebbet!", font=("Arial", 12))  # Üzenet, ha a tipp nagyobb, mint a kitalálandó szám

    def ranglista_felvetel(self):
        nev = simpledialog.askstring("Ranglista", "Add meg a neved:")  # Felugró ablakban a játékos nevének bekérése
        if nev:
            self.osszes_jatekos.append((nev, self.tippek_szama))  # Hozzáadja a játékost és a próbálkozásait a listához

    def mentes_txt(self):
        with open("ranglista.txt", "w") as file:
            for nev, probalkozasok in self.osszes_jatekos:
                file.write(f"{nev}: {probalkozasok} tippelés\n")  # Ranglista tartalmának kiírása TXT fájlba

    def megjelenit_ranglistat(self):
        ranglista_ablak = tk.Toplevel(self.root)
        ranglista_ablak.title("Ranglista")

        ranglista_cimke = tk.Label(ranglista_ablak, text="Ranglista", font=("Arial", 12))
        ranglista_cimke.pack()

        if self.osszes_jatekos:
            rendezett_ranglista = sorted(self.osszes_jatekos, key=lambda x: x[1])  # Ranglista rendezése próbálkozások száma szerint
            for nev, probalkozasok in rendezett_ranglista:
                ranglista_tekst = tk.Label(ranglista_ablak, text=f"{nev}: {probalkozasok} tippelés", font=("Arial", 12))
                ranglista_tekst.pack()
        else:
            uzenet = tk.Label(ranglista_ablak, text="Még nincs adat a ranglistában.", font=("Arial", 12))
            uzenet.pack()

def main():
    root = tk.Tk()
    root.title("Számkitaláló Játék")

    szamkitalalo_app = Szamkitalalo(root)

    root.mainloop()

if __name__ == "__main__":
    main()
