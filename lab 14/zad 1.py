liste_uprawnionych_pojazdow = []
liste_obecnych_pojazdow = []

class Parking():
    def __init__(self, rejestracja, miejsca):
        self.rejestracja = rejestracja
    miejsca = 30
    def dodaj_do_spisu(self):
        print("Dzein dobry! Witaj, Kup abonament na miejsce parkingowe")
        print("Wpish swoja tablice rejestracyjna w Formacie XXX-XXXXX")
        rejestracja = str(input())
        if rejestracja in liste_uprawnionych_pojazdow:
            print("Pojazd juz jest!")
        else:
            liste_uprawnionych_pojazdow.append(rejestracja)
            print("Pojazd zarejestrowany!")

    def usun_ze_spisu(self):
        print("Zakonczenie abonementu na miejsce parkingowe!")
        print("Wpish rejestracyje do useniecia w Formacie XXX-XXXXX")
        rejestracja = str(input())
        if rejestracja in liste_uprawnionych_pojazdow:
            print("Usunieto!")
        else:
            print("Nie ma takiego numera!")
            pass
class Pojazd(Parking):
    def __init__(self, rejestracja):
        super().__init__(rejestracja)

    def wjazd_na_parking(self, miejsca):
        print("Witaj, spawdzamy czy mozesz wjechac na parking!")
        if miejsca != 0:
            print("Jest wole miejsca, sprawdzamy subskrybcje!")
            if self.rejestracja in liste_uprawnionych_pojazdow:
                miejsca = miejsca - 1
                liste_obecnych_pojazdow.append(self.rejestracja)
            else:
                print("Nie morzesz wjechac, kup najpierw abonament!")
        else:
            print("Nie ma wolnuch miejsc!")
    def wyjazd_z_parkingu(self, miejsca):
        print("Witaj, wyjedz :)")
        liste_obecnych_pojazdow.remove(self.rejestracja)
        miejsca = miejsca + 1

autko1 = Pojazd('BCD-12376')
autko2 = Pojazd('DV-LUCKER')
autko3 = Pojazd('HCD-TANK')
autko4 = Pojazd('SKUTER-SUPER')
autko1.wjazd_na_parking()
autko2.wjazd_na_parking()
autko3.wjazd_na_parking()
autko1.wyjazd_z_parkingu()
autko4.wjazd_na_parking()
