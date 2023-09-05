v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int, input().split()))
    for i in range(1,len(tmp)-1,2):
        tree[tmp[0]].append([tmp[i],tmp[i+1]])
        
from collections import deque
def bfs(start) :
    visited = [False] * (v+1)
    q = deque([[start,0]])
    visited[start] = True
    dist = 0
    far = -1
    while q :
        node, weight = q.popleft()
        for next,w in tree[node]:
            if not visited[next]:
                if dist < weight + w:
                    dist = weight + w
                    far = next
                q.append([next,w+weight])
                visited[next] = True
    return far,dist

print(bfs(bfs(1)[0])[1])