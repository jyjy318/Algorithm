import time
import random
import heapq

def partition(v,a,b):
    pivot, i, j = v[b], a, b-1
    while i <= j:
        if v[i] <= pivot :
            i += 1
        else :
            v[i], v[j] = v[j], v[i]
            return i

def quickSort(v, a, b):
    if a>= b:
        return
    c = partition(v,a ,b)
    quickSort(v, a, c-1)
    quickSort(v, c+1, b)

random.seed(100)
n = int(input("n = "))
v = [random.randrange(100000000) for _ in range(n)]

ts = time.time()
heapq.heapify(v)
v = [heapq.heappop(v) for _ in range(len(v))]
et = int((time.time() - ts)*1000)
print(*v[:10])
print(f"Elapsed time is {et}ms.")
