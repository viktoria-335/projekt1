from evidencia_poistnych_udalosti import EvidenciaPoistnychUdalosti
from poisteny import Poisteny  

def menu():
    print("*********************************")
    print("Evidencia poistených osôb")
    print("*********************************")
    print("Vyberte možnosť:")
    print("1. Pridať nového poisteného")
    print("2. Vypísať všetkých poistených")
    print("3. Vyhľadať poisteného")
    print("4. Ukončiť aplikáciu")

def main():
    
    poistenci = [
        Poisteny("Ivan", "Novák", 50, "778678554"),
        Poisteny("Eva", "Šťastná", 25, "765453232")
    ]

    evidencia = EvidenciaPoistnychUdalosti()
    
    
    for poisteny in poistenci:
        evidencia.pridat_poisteneho(poisteny)

    while True:
        menu()
        volba = input("Vyberte možnosť (1/2/3/4): ")

        if volba == "1":
            meno = input("Zadajte meno: ")
            priezvisko = input("Zadajte priezvisko: ")
            vek = input("Zadajte vek: ")
            telefon = input("Zadajte telefónne číslo: ")
            poisteny = Poisteny(meno, priezvisko, vek, telefon)
            evidencia.pridat_poisteneho(poisteny)
            print("Poistený bol pridaný.")
            input("Pre ukončenie a návrat kliknite na ľubovoľné tlačítko...")

        elif volba == "2":
            evidencia.vypisat_vsetkych_poistenych()
            input("Pre ukončenie a návrat kliknite na ľubovoľné tlačítko...")

        elif volba == "3":
            meno = input("Zadajte meno poisteného: ")
            priezvisko = input("Zadajte priezvisko poisteného: ")
            najdeny = evidencia.vyhladat_poisteneho(meno, priezvisko)
            if najdeny:
                print("Nájdený poistený:")
                print(najdeny)
            else:
                print("Poistený s týmto menom a priezviskom nebol nájdený.")
            input("Pre ukončenie a návrat kliknite na ľubovoľné tlačítko...")

        elif volba == "4":
            print("Ukončujem aplikáciu.")
            break

        else:
            print("Neplatná voľba. Zadajte prosím číslo od 1 do 4.")
            input("Pre ukončenie a návrat kliknite na ľubovoľné tlačítko...")

if __name__ == "__main__":
    main()
