lista_uprawnionych_pojazdow = ['DBL-12345',"D8-LUCKER","HSD-TANK","SUPER-SKUTER"]
lista_obecnych_pojazdow = []
class Parking():
    def __init__(self,rejestracja):
        self.rejestracja = rejestracja
    def dodaj_do_spisu(self):
        print("Dzień dobry! Witaj, Kup abonament na miejsce parkingowe lol")
        print("Wpisz swoją tablicę rejestracyjną w formacie XXX-XXXXX")
        rejestracja = str(input())
        if rejestracja in lista_uprawnionych_pojazdow:
            print("Pojazd juz jest")
        else:
            lista_uprawnionych_pojazdow.append(rejestracja)
            print("pojazd zarejestrowany")
    def usun_ze_spisu(self):
        print("Zakończenie abonamentu na miejsce parkingowe")
        print("Wpisz rejestrację do usunięcia w formacie XXX-XXXXX")
        rejestracja = str(input())
        if rejestracja in lista_uprawnionych_pojazdow:
            lista_uprawnionych_pojazdow.remove(rejestracja)
            print("Usunięto")
        else:
            print("Nie ma takiego numeru")
            pass
class pojazd(Parking):
    miejsca = 3
    def __init__(self, rejestracja):
        super().__init__(rejestracja)
    def wjazd_na_parking(self):
        print("Witaj, sprawdzamy czy możesz wjechać na parking.")
        if pojazd.miejsca !=0:
            print("Są wolne miejsca, sprawdzamy subskrybcje")
            if self.rejestracja in lista_uprawnionych_pojazdow:
                print("Możesz wjechać, miłego dnia")
                pojazd.miejsca = pojazd.miejsca - 1
                lista_obecnych_pojazdow.append(self.rejestracja)
            else:
                print("Nie mozesz wjechać, kup najpierw abonament")
        else:
            print("nie ma wolnych miejsc")
    def wyjazd_z_parkingu(self):
        print("Witaj, wyjedź sobie czy coś")
        lista_obecnych_pojazdow.remove(self.rejestracja)
        pojazd.miejsca = pojazd.miejsca + 1
autko1 = pojazd("DBL-12345")
autko2 = pojazd("D8-LUCKER")
autko3 = pojazd("HSD-TANK")
autko4 = pojazd("SUPER-SKUTER")
autko1.wjazd_na_parking()
autko2.wjazd_na_parking()
autko3.wjazd_na_parking()
autko1.wyjazd_z_parkingu()
autko4.wjazd_na_parking()
print(lista_obecnych_pojazdow)