import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
dp = [1] * n
for i in range(1,n):
	for j in range(0,i):
		if num[i] > num[j]:
			dp[i] = max(dp[j]+1, dp[i]) 
print(max(dp))
# 1 2 5 4 5 6
