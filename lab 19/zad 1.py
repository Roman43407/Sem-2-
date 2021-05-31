kod = input("Podaj kod pocztowy w oznaczeniu(PL/pl-xxxxx): ")

def Add(kod, file):
     file.write(kod)
     file.close()

try:
    file = open('kodPocztowy.txt', 'w')
    if kod[0] == "P" or "p":
        if kod[1] == "L" or "l":
            Add(kod, file)
except FileNotFoundError:
    print("to nie jest kod pocztowy Polski")