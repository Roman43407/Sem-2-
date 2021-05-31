class Smartfon:
    def __init__(self, brand, wersja, age, kolor, numer, gb, cena):
        self.brand = brand
        self.wersja = wersja
        self.age = age
        self.kolor = kolor
        self.gb = gb
        self.numer = numer
        self.cena = cena

    def SayMyName(self):
        print(self.brand)
        print(self.wersja)
        print(self.age)
        print(self.kolor)
        print(self.gb)
        print(self.numer)
        print(self.cena)
nowySmartfon = Smartfon("Iphon", "7 plus", "2016", "Silver", "0996494521", "128 gb", "1697 zł\n")
smart = []
def Main():
    smart.append(nowySmartfon)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie: ")
        if choice == "Tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Chcesz dodać nowy telefon, przejrzeć listę telefonów czy usunąć go z listy? wybierz:\n 1 - Dodać nowy telefon, 2 - Wyświetlić listę telefonów, 3 - usunąć: ")
    if (choice == "1"):
        AddSmart()
    elif (choice == "2"):
        ShowSmart()
    else:
        RemoveSmart()
def AddSmart():
    brand = input("Podaj markę: ")
    wersja = int(input("Podaj wersję: "))
    age = int(input("Podaj rok: "))
    kolor = input("Podaj kolor: ")
    numer = int(input("Podaj numer telefonu: "))
    gb = int(input("Podaj liczbę GB: "))
    cena = int(input("Podaj cenę: "))
    smartfon = Smartfon(brand, wersja, age, kolor, numer, gb, cena)
    print("Dodano nowy telefon!")
    smart.append(smartfon)

def ShowSmart():
    smart.sort(key=SortKey)
    for i in smart:
        i.SayMyName()
def SortKey(obj):
    return obj.brand
def RemoveSmart():
    choice = int(input("podaj indeks smartfonu: "))
    yesOrNot = input("Czy na pewno chcesz usunąć smartfon: tej operacji nie będzie można cofnąć! Tak/Nie".format(choice))
    if yesOrNot == "Tak":
        smart.pop(choice)
        ShowSmart()
Main()