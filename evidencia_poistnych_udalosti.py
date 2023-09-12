class EvidenciaPoistnychUdalosti:
    def __init__(self):
        self.poisteni = []

    def pridat_poisteneho(self, poisteny):
        self.poisteni.append(poisteny)

    def vypisat_vsetkych_poistenych(self):
        for poisteny in self.poisteni:
            print(poisteny)

    def vyhladat_poisteneho(self, meno, priezvisko):
        for poisteny in self.poisteni:
            if poisteny.meno == meno and poisteny.priezvisko == priezvisko:
                return poisteny
        return None


