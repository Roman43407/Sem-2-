import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Pogoda")
root.geometry('400x200')
root["bg"] = "lightblue"

Label(root, text = 'Aplikacja pogodowa', font = 'Consolas 15 bold', bg = 'lightblue').pack(pady = 5)
Label(root, text = 'Wpisz nazwę miasta:', font = 'Consolas 11 bold', bg = 'lightblue').pack(pady = 5)

city = Entry(root, width = 40)
city.pack()

def temp():
    a = str(city.get())
    search = f'Pogoda w {a}'

    url = f"https://www.google.com/search?&q={search}"

    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    upadate = s.find("div", class_= "BNeawe").text

    messagebox.showinfo("Pogoda", "W miasteczku " + a + " temperatura " + upadate)

    city.delete(0, END)

Button(root, text = "Informacje o pogodzie", command = temp).pack(pady = 5)

root.mainloop()