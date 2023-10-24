t = int(input())
for _ in range(t):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append([0]+list(map(int, input().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    for i in range(2,n+1):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2])+sticker[0][i]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2])+sticker[1][i]
    print(max(dp[0][n],dp[1][n]))