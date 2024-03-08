import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[10001] * (n+1) for _ in range(n+1)]
edge = []
for start, end, time in [list(map(int, input().split())) for _ in range(m)] :
    edge.append([start, end, time])
    graph[start][end] = min(time, graph[start][end])
    
minDist = [float('inf')] * (n+1)
minDist[1] = 0
cycle = False
for i in range(n):
    for start, end, time in edge :
        if minDist[end] > minDist[start] + time :
            minDist[end] = minDist[start] + time
            if i == n-1 :
                cycle = True
if cycle : print(-1)
else:
    for x in minDist[2:] :
        print(x) if x != float('inf') else print(-1)