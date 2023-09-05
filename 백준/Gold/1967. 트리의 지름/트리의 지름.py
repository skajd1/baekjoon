# 가장 먼 두 노드 찾기
n = int(input())
tree = [[] for _ in range(n+1)]
for p,c,w in [map(int, input().split()) for _ in range(n-1)]:
    tree[p].append([c,w])
    tree[c].append([p,w])

from collections import deque

def bfs(start) :
    visited = [False] * (n+1)
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