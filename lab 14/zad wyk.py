superhero_list = []
import random
class Superhero:
    def __init__(self, rasa, predkosc , imie, sila):
        self.rasa = rasa
        self.predkosc = predkosc
        self.imie = imie
        self.sila = sila
    def atak(self):
        print("Superbohater {} uderza z siłą {} niutony".format(self.imie, self.sila))
    def biegnij(self):
        print("Superbohater {} biegnie z prędkością {} km/h".format(self.imie, self.predkosc))

class Spiderman(Superhero):
    def __init__(self, rasa, predkosc , imie, sila):
        super().__init__(rasa, predkosc , imie, sila)
    def strzel_pajeczyna(self):
        print("Spiderman strzela pajęczyną.")
    def walka_wrecz(self, przeciwnik):
        print("Spiderman walczy z {}".format(przeciwnik))
        wynik = random.randint(0, 100)
        if wynik > 50:
            print("Spiderman wygrał.")
        elif wynik < 50:
            print("Spiderman przegrał.")
        else:
            print("Remis")

spiderman = Spiderman("czlowiek", 32, "Spiderman", 23)
spiderman.strzel_pajeczyna()
spiderman.walka_wrecz("Venom")

class IronMan(Superhero):
    def __init__(self, rasa, predkosc , imie, sila):
        super().__init__(rasa, predkosc , imie, sila)
    def superzdolnosc(self):
        print("Kombinezon oraz Gadżety")
    def osobowosc(self):
        print("Narcyz")
    def nemezis(self):
        print("Ultron/ Iron Monger / Whiplash")

IronMan = IronMan("czlowiek", "Prędkość kombinezonu", "Tony Stark", "Siła kombinezonu")
IronMan.superzdolnosc()
IronMan.osobowosc()
IronMan.nemezis()

class Thor(Superhero):
    def __init__(self, rasa, predkosc, imie, sila):
        super().__init__(rasa, predkosc, imie, sila)

    def piorunemgo(self):
        print("Piorun pier, pier... Nie będę mówił jak. Thor to zrobił. Tak się przestraszyłem, że hej!")

    def mjolnir(self):
        print("Thor uderza młotkiem w brata Lokiego")
        print("Wziął i go zabił no.")

    def Odyn(self):
        print("{} mówi ojcu, że nie jest gotowy objąć tron.".format(self.imie))

    def identyfikacja(self):
        print("Ja jestem {}, {} !".format(self.imie, self.rasa))


Thor = Thor("Bógpiorunów", 30, "Thor", 9000)
Thor.atak()
Thor.piorunemgo()
Thor.mjolnir()
Thor.Odyn()
Thor.identyfikacja()

class Wolverine(Superhero):
    def __init__(self,rasa,predkosc,imie,sila):
        super().__init__(rasa,predkosc,imie,sila)
    def walka(self):
        tab_enemy = ["Sabertooth", "Deadpool", "Magneto"]
        return tab_enemy
    def atak_pazurami(self,tab_enemy):
        dmg = random.randint(30,60)
        rand_enemy = random.choice(tab_enemy)
        print(f"{self.imie} atakuje {rand_enemy}!")
        print(f"Zadał {dmg} obrażeń.")
        if dmg <= 40:
            print("Nie jest to super efektywne.")
        elif 40 <= dmg <= 50:
            print("Niezły atak!")
        else:
            print("Jest super efektywny!")

Wolverine = Wolverine("Człowiek", 30, "Logan", 50)
Wolverine.atak_pazurami(Wolverine.walka())