import sys

H, W = map(int,sys.stdin.readline().split())
heights = list(map(int,sys.stdin.readline().split()))
answer = 0

for i in range(1,W-1) :
    left = max(heights[:i])
    right = max(heights[i+1:])
    temp = min(left,right)
    if temp > heights[i] :
        answer += temp - heights[i]
print(answer)