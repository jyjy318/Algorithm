import time
import random

def selectionSort(v):
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if v[m] > v[j]:
                m = j
            v[m], v[i] = v[i], v[m]

random.seed(100)
n = int(input("n = "))
v = [random.randrange(1000000) for _ in range(n)]

ts = time.time()
selectionSort(v)
et = int((time.time() - ts)*1000)
print(f"Elapsed time is {et}ms.")
