class Obywatel:
    def __init__(self, name, surname, street, num_home, zip_code, locality):
        self.name = name
        self.surname = surname
        self.street = street
        self.num_home = num_home
        self.zip_code = zip_code
        self.locality = locality

    def SayMyName(self):
        print('===================')
        print(self.name, self.surname)
        print(self.street, self.num_home)
        print(self.zip_code, self.locality)
        print('===================')

nowyObywat = Obywatel("Roma", "Romanets", "st.Luseka", 7, 4770, "Kiev")
Ulic = []
def Main():
    Ulic.append(nowyObywat)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie: ")
        if choice == "Tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Co chcesz robić?\n1 - Dodacz nowego syudenta, 2 - Wyświetlić listę uczniów, 3 - Usunąć z listy: ")
    if (choice == "1"):
        AddUlic()
    elif (choice == "2"):
        ShowUlic()
    else:
        RemoveUlic()
def AddUlic():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    street = input("Podaj ulicę: ")
    num_home = int(input("Podaj numer domu: "))
    zip_code = int(input("Podaj indeks kraju / miasta: "))
    locality = input("Podaj nazwę miasta: ")
    Obywat = Obywatel(name, surname, street, num_home, zip_code, locality)
    print("Dodano nowy adres!")
    Ulic.append(Obywat)

def ShowUlic():
    Ulic.sort(key=SortKey)
    for i in Ulic:
        i.SayMyName()
def SortKey(obj):
    return obj.name
def RemoveUlic():
    choice = int(input("podaj indeks Domu: "))
    yesOrNot = input("Czy na pewno chcesz usunąć adres domu: tej operacji nie będzie można cofnąć! Tak/Nie: ".format(choice))
    if yesOrNot == "Tak":
        Ulic.pop(choice)
        ShowUlic()
Main()
