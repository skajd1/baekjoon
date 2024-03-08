import sys
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())
questions = [list(map(int, input().split())) for _ in range(m)]

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i] = 1
for i in range(1,n):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
for i in range(2, n+1) :
    for j in range(1,n-i+1):
        # print(j, i+j)
        if arr[j] == arr[i+j] and dp[j+1][i+j-1] : dp[j][i+j] = 1

for s,e in questions:
    print(dp[s][e])