n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for x,y in [map(int, input().split()) for _ in range(n-1)] :
    graph[x].append(y)
    graph[y].append(x)
q = [1]
parent[1] = 1
while q :
    node = q.pop()
    for x in graph[node] :
        if not parent[x] :
            parent[x] = node
            q.append(x)

print(*parent[2:],sep='\n')