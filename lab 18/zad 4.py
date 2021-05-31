import os
import heapq as hs
from timeit import default_timer as timer
start = timer()
# Sortowanie szybkie:
sort1 = [4, 10, 11, 5, 73, 5, 1]
print(sort1)
print("Sortowanie szybkie: ")
sort1.sort()
print(sort1)
end = timer()
print(end - start)
print("\n")
start = timer()
# Sortowanie Heap:
sort2 = [4, 10, 11, 5, 73, 5, 1]
print(sort2)
print("Heap Sort: ")
hs.heapify(sort2)
print(sort2)
end = timer()
print(end-start)