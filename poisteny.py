class Poisteny:
    def __init__(self, meno, priezvisko, vek, telefonne_cislo):
        self.meno = meno
        self.priezvisko = priezvisko
        self.vek = vek
        self.telefonne_cislo = telefonne_cislo

    def __str__(self):
        return f"Meno: {self.meno}, Priezvisko: {self.priezvisko}, Vek: {self.vek}, Telefónne číslo: {self.telefonne_cislo}"