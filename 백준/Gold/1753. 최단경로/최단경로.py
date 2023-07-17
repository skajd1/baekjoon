import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline
node_num,edge_num = map(int, input().split())
nodeStart = int(input())
edgeInfo = [list(map(int, input().split())) for _ in range(edge_num)]
distance = [float('inf')] * (node_num + 1)

graph = defaultdict(list)
for u,v,w in edgeInfo :
    graph[u].append((v,w))
distance[nodeStart] = 0
q = [(0,nodeStart)]
while q :
    current_dist, current_node = heappop(q)
    # 현재 방문한 노드로부터 연결돼있는 노드 까지 거리 => w
    for v,w in graph[current_node] : 
        if distance[v] > current_dist + w :
            distance[v] = current_dist + w
            heappush(q,(distance[v],v))
        
for x in distance[1:] :
    print(x if x != float('inf') else "INF") 
            
