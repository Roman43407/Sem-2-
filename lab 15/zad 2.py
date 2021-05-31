class Shop:
    def __init__(self, name, brewery, type_of_beer, price, category, ABV):
        self.name = name
        self.brewery = brewery
        self.type_of_beer = type_of_beer
        self.price = price
        self.category = category
        self.ABV = ABV

    def SayMyName(self):
        print("Nazwe: ", self.name,)
        print("Browar: ", self.brewery)
        print("Type of beer: ", self.type_of_beer)
        print("Cena: ", self.price)
        print("Category: ", self.category)
        print("ABV: ", self.ABV)

nowePiwko = Shop("Heineken", "Zywiec", "Lager", 4.99, "Alkoholowe", "4.8%\n")
nowePiwko2 = Shop('Warka', 'Warka', 'Lager', 2.99, 'Alkoholowe', '5.2%\n')
piwko = []
def Main():
    piwko.append(nowePiwko)
    piwko.append(nowePiwko2)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie: ")
        if choice == "Tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Co chcesz robić?\n1 - Dodaj nowe piwo do baru, 2 - Wyświetlić listę Piwka, 3 - Usunąć z listy piwko: ")
    if (choice == "1"):
        Addpiwko()
    elif (choice == "2"):
        Showpiwko()
    else:
        Removepiwko()
def Addpiwko():
    name = input("Podaj nazwe: ")
    brewery = input("Podaj browar: ")
    type_of_beer = input("Podaj rodzaj piwa: ")
    price = int(input("Podaj cene: "))
    category = input("Podaj kategory(Alkoholowe/Niealkoholowe):")
    ABV = int(input("Podaj ABV: "))
    Piwko = Shop(name, brewery, type_of_beer, price, category, ABV)
    print("Dodano nowe Piwko!")
    piwko.append(Piwko)

def Showpiwko():
    piwko.sort(key=SortKey)
    for i in piwko:
        i.SayMyName()
def SortKey(obj):
    return obj.name
def Removepiwko():
    choice = int(input("podaj indeks piwa: "))
    yesOrNot = input("Czy na pewno chcesz usunąć studenta: tej operacji nie będzie można cofnąć! Tak/Nie".format(choice))
    if yesOrNot == "Tak":
        piwko.pop(choice)
        Showpiwko()
Main()