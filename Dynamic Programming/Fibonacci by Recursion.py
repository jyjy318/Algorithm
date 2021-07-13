k = int(input(" k = "))

def fi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fi(n-1) + fi(n-2)

print(fi(k))
