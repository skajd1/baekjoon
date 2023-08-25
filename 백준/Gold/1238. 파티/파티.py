from heapq import heappop, heappush
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for s,e,t in [map(int, input().split()) for _ in range(m)]:
    graph[s].append([e,t])
dist = [[float('inf')] * (n+1) for _ in range(n+1)] # i 가 x 까지 가는 최단 시간

def dijk(start):
    global dist
    q = [[0, start]]
    while q :
        cur, node = heappop(q)
        if dist[start][node] < cur : continue
        for v,w in graph[node]:
            if dist[start][v] > cur + w :
                dist[start][v] = cur + w
                heappush(q, [dist[start][v],v])
    dist[start][start] = 0
for i in range(1,n+1) :
    dijk(i)


print(max([dist[i][x] + dist[x][i] for i in range(1,n+1)]))