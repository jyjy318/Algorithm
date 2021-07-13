K = int(input("k : "))
coins = list(map(int, input().split()))

print(K)
print(coins)

dp = [0]*(K+1)
dp[0] = 1
for coin in coins:
    for i in range(K, -1, -1):
        sum = dp[i]
        for j in range(i-coin, -1, -coin):
            sum += dp[j]
        dp[i] = sum

print(dp[K])
