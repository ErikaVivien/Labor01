# kattintas szamolo
import tkinter as tk

class KattintasSzamolo:
    def __init__(self, root):
        self.root = root
        self.kattintasok_szama = 0

        self.label = tk.Label(root, text="Kattintások száma: 0")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Kattints ide!", command=self.kattintas_novel)
        self.button.pack()

    def kattintas_novel(self):
        self.kattintasok_szama += 1
        self.label.config(text=f"Kattintások száma: {self.kattintasok_szama}")

def main():
    root = tk.Tk()
    root.title("Kattintások számláló")

    app = KattintasSzamolo(root)

    root.mainloop()

if __name__ == "__main__":
    main()
