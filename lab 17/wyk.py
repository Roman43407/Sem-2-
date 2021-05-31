import heapq

sort = [18, 1, 123, 345534, 13, 5, 345, 54, 31, 8]
print("Lista wejściowa to:")
print(sort)
sort.sort()
print(sort)
Heapsort = [18, 1, 123, 345534, 13, 5, 345, 54, 31, 8]
heapq.heapify(sort)
print(sort)