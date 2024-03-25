import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def getMinDist(start) -> list :
    dist = [int(1e9)] * (v+1)
    dist[start] = 0
    q = []
    heappush(q,[0,start])
    while q :
        nowDist, node = heappop(q)
        for nextNode, d in enumerate(graph[node]) :
            if dist[nextNode] > dist[node] + d :
                dist[nextNode] = dist[node] + d
                heappush(q, [d,nextNode])
    return dist
for t in range(1, int(input()) + 1) :
    ans = []
    v,e,c = map(int, input().split())
    s,g,h = map(int, input().split())
    graph = [[int(1e9)] * (v+1) for _ in range(v+1)]
    candidate = []
    for start, end, dist in [map(int, input().split()) for _ in range(e)] :
        graph[start][end] = dist
        graph[end][start] = dist
    for _ in range(c):
        candidate.append(int(input()))
    # 각 목적지까지의 최단거리인 경로를 구하고 거기에 g,h가 포함돼있으면 그 목적지는 정답임
    minDistFromStart = getMinDist(s)
    gh_dist = graph[g][h]
    graph[g][h] = 0
    graph[h][g] = 0
    mergedNode = min(g,h)
    minDistFromGH = getMinDist(mergedNode)
    # gh로부터 목적지까지의 최단거리 + gh 거리 + gh부터 s까지의 최단거리 == s부터 목적지까지의 거리 이면 ans !
    # 만약 목적지가 gh에 포함이면 gh거리 더하지 않기
    for x in candidate :
        dist = minDistFromGH[x] + gh_dist + minDistFromGH[s]
        if minDistFromStart[x] == dist : ans.append(x)

    print(*sorted(ans))