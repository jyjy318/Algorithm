def ti1(n):
    t = [ 1,1]
    for i in range(2,n+1):
        t. append(t[-1]+2*t[-2])
    return t[n]


def ti2(n):
    global dp
    if n == 0:
        return 1
    if n == 1:
        return 1
    if dp[n] == None:
        return dp[n]
    dp[n] = ti2(n-1) + 2*ti2(n-2)
    return dp[n]

def ti3(n):
    return (2 **(n+1) + 2*(1 if n %2 == 0 else -1))//3

n = int(input("n = :"))
print(ti1(n))
dp = [None]*(n+1)
print(ti2(n))
print(ti3(n))
