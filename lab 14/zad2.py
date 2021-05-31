animal_list = []
import random
class Kat:
    def __init__(self, rasa, imie, waga):
        self.rasa = rasa
        self.imie = imie
        self.waga = waga
    def atak(self):
        print("SuperKot{} rasy {}. ".format(self.imie, self.rasa))
    def biegnij(self):
        print("SuperKot {} ma wagę {} kg".format(self.imie, self.waga))

class Dog(Kat):
    def __init__(self, rasa, imie, waga):
        super().__init__(rasa, imie, waga)
    def Pies_szczeka(self):
        print("Pies szczeka!")
    def walka_wrecz(self, przeciwnik):
        print("Max walczy z {}".format(przeciwnik))
        wynik = random.randint(0, 100)
        if wynik > 50:
            print("Max wygrał.")
        elif wynik < 50:
            print("Max przegrał.")
        else:
            print("Remis")

dog = Dog("Labrador", "Max", 32)
dog.Pies_szczeka()
dog.walka_wrecz("Boris")

class Fish(Kat):
    def __init__(self, rasa, imie, waga):
        super().__init__(rasa, imie, waga)
    def superzdolnosc(self):
        print("echolocator")
    def osobowosc(self):
        print("Narcyz")

fish = Fish("Błazenek", "Nema", "100g")
fish.superzdolnosc()
fish.osobowosc()

class Bird(Kat):
    def __init__(self, rasa, imie, waga):
        super().__init__(rasa, imie, waga)

    def Odyn(self):
        print("{} mówi, że lubi złoto xD".format(self.imie))

    def identyfikacja(self):
        print("Ja jestem {}, {} !".format(self.imie, self.rasa))


b = Bird("Kruk", "Bloodhound", "500g")
b.Odyn()
b.identyfikacja()