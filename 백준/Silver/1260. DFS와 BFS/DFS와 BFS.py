import sys
input = sys.stdin.readline
n,m,v = map(int, input().split())

edge = dict()
visited1 = [0] * (n+1)
visited2 = [0] * (n+1)
tmp = []
for _ in range(m):
	tmp.append(list(map(int, input().split())))
for i in range(n):
  edge[i+1] = []
for s,e in tmp:
	edge[s].append(e)
	edge[e].append(s)
for i in range(n):
	edge[i+1].sort()
#bfs
order1 = []
from collections import deque
q = deque([v])
visited1[v] = 1
while q:
	node = q.popleft()
	order1.append(node)
	for x in edge[node]:
		if not visited1[x] :
			visited1[x] = 1
			q.append(x)
#dfs
order2 = []
def dfs(v):
	if not visited2[v] :
		visited2[v] = 1
		order2.append(v)
		for x in edge[v]:
			dfs(x)
dfs(v)

print(*order2)
print(*order1)
			
