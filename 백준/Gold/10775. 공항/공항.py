import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
ans = 0
parent = {i : i for i in range(g+1)}

def find_parent(x):
    if parent[x] == x :
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
def union(x,y):
    x = find_parent(x)
    y = find_parent(y)
    parent[y] = x

for plane in planes:
    now = find_parent(plane)
    if now == 0 :
        break
    ans += 1
    union(now-1,now)

print(ans)
