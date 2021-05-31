import random
from timeit import default_timer as timer
start = timer()
stos = []
kolejka = []
for i in range(50):
    stos.append(random.randint(0,100))
print("Stos: ", stos)
end = timer()
print(end - start)
print("\n")
start = timer()
for elements in stos:
    kolejka.insert(0, elements)
print("Kolejka: ", kolejka)
end = timer()
print(end-start)