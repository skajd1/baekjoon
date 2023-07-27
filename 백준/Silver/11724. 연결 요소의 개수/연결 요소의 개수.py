import sys
input = sys.stdin.readline
n,m = map(int, input().split())

edgeInfo = [list(map(int, input().split())) for _ in range(m)]
node = [[] for _ in range(n)]
for u,v in edgeInfo:
	node[u-1].append(v)
	node[v-1].append(u)
from collections import deque
visited=[0] * n
ans = 0
for j in range(1,n+1):
	q = deque([j])
	if not visited[j-1] :
		visited[j-1] = 1
		ans += 1
	while q:
		x = q.popleft()
		for i in node[x-1] :
			if not visited[i-1]:
				visited[i-1] = 1
				q.append(i)
print(ans)