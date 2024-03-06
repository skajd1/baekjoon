import sys

def findMin(k,files,sums):
    dp = [[0] *(k+1) for _ in range(k+1)]
    #dp[i][j] 는 i부터 j까지의 합의 최소값
    for i in range(1,k+1):
        for j in range(1,k+1):
            if i+1 == j : dp[i][j] = sums[j-1]-sums[i-1-1]
    for i in range(2, k) :
        for j in range(1,k-i+1):
            dp[j][j+i] = sums[j+i-1] - sums[j-1-1] + min([dp[j][j+x] + dp[j+x+1][j+i] for x in range(i)])
    return dp[1][k]


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    sums = []
    s = 0
    for file in files :
        s += file
        sums.append(s)
    sums.append(0)
    print(findMin(k,files,sums))