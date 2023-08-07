from collections import deque
n, k = map(int, input().split())
num = deque([i for i in range(1,n+1)])
ans = []
while num:
    for _ in range(k-1):
        num.rotate(-1)
    ans.append(num.popleft())
print("<",end = "")
print(*ans,sep = ", ",end="")

print(">")