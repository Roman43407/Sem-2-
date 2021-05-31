class Book:
    def __init__(self, author, title, frame, pages, exampleText):
        self.title = title
        self.author = author
        self.frame = frame
        self.pages = pages
        self.exampleText = exampleText

    def SayMyName(self):
        print(self.author)
        print(self.title)
        print(self.frame)
        print(self.pages)
        print(self.exampleText)
nowaKsiazka = Book("Sapkowski Andrzej", "Wiedźmin - ostatnie rozszczenie", "hard", 300, "jakiś tekst")
books = []
def Main():
    books.append(nowaKsiazka)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie: ")
        if choice == "Tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Czy chcesz dodać nową książke, wyświetlić listę obecnie istniejących książek lub usunąć jedną z nich?\n1 - Dodać nową książke, 2 - wyświetlić listę, 3 - usunąć: ")
    if (choice == "1"):
        AddBook()
    elif (choice == "2"):
        ShowBooks()
    else:
        RemoveBook()
def AddBook():
    author = input("Podaj autora: Nazwisko Imie")
    title = input("Podaj tytuł")
    frame = input("Podaj rodzaj oprawy")
    pages = int(input("Podaj ilość stron"))
    exampleText = input("Podaj przykładowy fragment tekstu")
    book = Book(author, title, frame, pages, exampleText)
    print("Dodano nową książke!")
    books.append(book)

def ShowBooks():
    books.sort(key=SortKey)
    for i in books:
        i.SayMyName()
def SortKey(obj):
    return obj.author
def RemoveBook():
    choice = int(input("podaj indeks książki: "))
    yesOrNot = input("Czy na pewno chcesz usunąć książke: tej operacji nie będzie można cofnąć! Tak/Nie".format(choice))
    if yesOrNot == "Tak":
        books.pop(choice)
        ShowBooks()
Main()