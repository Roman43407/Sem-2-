class Student:
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    def SayMyName(self):
        print("Imię: ", self.name)
        print("Nazwisko: ", self.surname)
        print("Wiek: ", self.age)
        print("Narodowość: ", self.country)

nowyStudent = Student("Roman", "Romanets", "18", "Ukraine\n")
stud = []
def Main():
    stud.append(nowyStudent)
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
        Addstud()
    elif (choice == "2"):
        Showstud()
    else:
        Removestud()
def Addstud():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    age = int(input("Podaj swój wiek: "))
    country = input("Podaj swoją narodowość: ")
    Studen = Student(name, surname, age, country)
    print("Dodano nowego ucznia!")
    stud.append(Studen)

def Showstud():
    stud.sort(key=SortKey)
    for i in stud:
        i.SayMyName()
def SortKey(obj):
    return obj.name
def Removestud():
    choice = int(input("podaj indeks studenta: "))
    yesOrNot = input("Czy na pewno chcesz usunąć studenta: tej operacji nie będzie można cofnąć! Tak/Nie".format(choice))
    if yesOrNot == "Tak":
        stud.pop(choice)
        Showstud()
Main()