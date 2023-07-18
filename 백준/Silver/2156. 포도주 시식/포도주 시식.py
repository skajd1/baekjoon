import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[0], dp[1] = l[0], sum(l[:2])
for i in range(2, n):
	dp[i] = max(dp[i-2] + l[i], l[i] + l[i-1] + dp[i-3] , dp[i-1])

print(dp[n-1])