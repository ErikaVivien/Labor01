class Jelszo():
    jelszo = ""

    def __init__(self):
        pass
    def jelszo_bekerese(self):
        pass

    def jelszo_ellenorzese(self):
        pass

    def jelszo_generalasa(self, hossz, nagybetu, kisbetu, szam):
        import string
        import random
        karakterek = ""
        if nagybetu:
            karakterek = karakterek + string.ascii_uppercase
        if kisbetu:
            karakterek = karakterek + string.ascii_lowercase
        if szam:
            karakterek = karakterek + string.digits
        jelszo = ""
        for i in range(hossz):
            jelszo = jelszo + karakterek[random.randint(0, len(karakterek) - 1)]

        return jelszo
class Felhasznalo():
    pass

pw = Jelszo()
print(pw.jelszo_generalasa(10, True, True, True))