n,k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])
dp = [0] * (k+1)
# dp[i] = i원을 만드는 경우의 수  dp
dp[0] = 1
for coin in coins:
    for i in range(1,k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
print(dp[k])