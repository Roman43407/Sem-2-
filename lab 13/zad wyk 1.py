class bird:

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek

        self.szybkosc = szybkosc

    def fly(self):
        print("Tu", self.gatunek, "! Lecimy i osiągniemy prędkość ", self.szybkosc)


class eagle(bird):

    def __init__(self, szybkosc):
        super().__init__("orzeł", szybkosc)

    def attack(self):
        print("Tu", self.gatunek, "! DO ATAKU")


class penguin(bird):

    def __init__(self, szybkosc):
        super().__init__("pingwin", szybkosc)

    def slide(self):
        print("Tu", self.gatunek, ".Bziuuuuum")

    def fly(self):
        print("Tu", self.gatunek, ". Nie potrafie latać kurde faja :(")


class kukulka(bird):

    def __init__(self, szybkosc):
        super().__init__(self, szybkosc)

    def latanko(self):
        print("Tu ", self.gatunek, ". Latam sobie latam! Tak o szybko! O:", self.szybkosc)

    def jajeczko(self):
        print("Znów ", self.gatunek, "! Widze gniazdo więc podrzcam tam jajka O")


kukuleczka = kukulka(35)

kukuleczka.latanko()

kukuleczka.jajeczko()