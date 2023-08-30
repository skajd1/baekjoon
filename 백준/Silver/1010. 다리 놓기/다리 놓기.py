t = int(input())
for _ in range(t):
    m,n = map(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][0] = 1
    dp[1][1] = 1
    for i in range(2,n+1):
        for j in range(m+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    print(dp[n][m])