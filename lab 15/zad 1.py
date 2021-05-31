class Restaurant:
    def __init__(self, nazwa, lokacja):
        self.nazwa = nazwa
        self.lokacja = lokacja
class IceCreamStand(Restaurant):
    def __init__(self, nazwa, lokacja, menu):
        super().__init__(nazwa, lokacja)
        self.menu = menu
    def smaki(self):
        print("To destempne smaki w lodziarni: ")
        print(self.menu)
    def mieszanie(self):
        print("Witaj w mieszalni smakow lodow!")
        print("Powiedz, jaki smaki chcesz miec w lodach: ")
        print(self.menu)
        wybur = int(input("Wybierz je prosze po indekszch z listy wyzej. Jesli skonczyles mieszanie, wybierz opcje 0.\n= "))
        if wybur != 0:
            if wybur == 1:
                print("Wybrales smaki :", smakilodziarnia[0])
                smaki = smakilodziarnia[0]
                wybur2 = int(input("Wybierz prosze kolejny smak: "))
                if wybur2 == 1:
                    print("Juz wybralesz ten smak, koncze mieszanie")
                elif wybur2 == 2:
                    print("Wybrales smak :", smakilodziarnia[1], "Dodaje do mieszanki")
                    smaki += smakilodziarnia[1]

                if wybur == 2:
                    print("Wybrales smak :", smakilodziarnia[1])
                if wybur == 3:
                    print("Wybrales smak :", smakilodziarnia[2])
            else:
                pass
smakilodziarnia = ("1. Wanilowe", "2. Czekoladowe", "3. Truskawkowe")
Lodzearnia = IceCreamStand("Lody dla ochlody", "Centrum miasta", smakilodziarnia)
Lodzearnia.mieszanie()
