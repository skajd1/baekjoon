n,k = map(int, input().split()) # n : 동전 종류 k : 만들어야 하는 금액
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [[float('inf')] * (k+1) for _ in range(n+1)]
# dp[i][j] : i번째까지의 동전을 사용해 j원을 만들 때 사용된 동전의 최소 개수
for i in range(1 , n+1):
    for j in range(1, k+1):
        if j%coins[i-1] == 0 :
            dp[i][j] =  j//coins[i-1]
        elif j-coins[i-1] > 0:
            dp[i][j] = min(dp[i-1][j],dp[i][j], dp[i][j-coins[i-1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]


print(dp[n][k] if dp[n][k] != float('inf') else -1)