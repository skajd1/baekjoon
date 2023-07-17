from collections import defaultdict
from heapq import heappop, heappush
import sys

input = sys.stdin.readline
n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for u,v,w in (list(map(int, input().split())) for _ in range(e)):
    graph[u].append((v,w))
    graph[v].append((u,w))
v1,v2 = map(int, input().split())

# 1 -> v1 - > v2 -> n

# 1 -> v2 - > v1 -> n

def dijk(startNode):
    global graph
    distance = [float('inf')] * (len(graph) + 1)
    distance[startNode] = 0
    q = [(0,startNode)]

    while q :
        current_dist, current_node = heappop(q)
        if distance[current_node] < current_dist :
            continue
        for v,w in graph[current_node] :
            if distance[v] > current_dist + w :
                distance[v] = current_dist + w
                heappush(q,(distance[v],v))


    return distance

dist_first = dijk(1)
dist_v1 = dijk(v1)
dist_v2 = dijk(v2)
answer = min(dist_first[v1] + dist_v1[v2] + dist_v2[n], dist_first[v2] + dist_v2[v1] + dist_v1[n])

print(answer if answer != float('inf') else -1)
