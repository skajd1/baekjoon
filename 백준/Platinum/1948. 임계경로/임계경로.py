# 최장거리와 1분도 쉬지않고 가야하는 도로 갯수 카운트
n = int(input())
m = int(input())
graph = [[[] for _ in range(n+1)] for _ in range(2)]
for s,e,t in list(map(int, input().split()) for _ in range(m)):
    graph[0][s].append([e,t])
    graph[1][e].append([s,t])
start, end = map(int, input().split())
#bfs
#최장거리인 q를 빠져나오면 그 인덱스 들을 카운트
from collections import deque
arrive = [0] * (n+1)

q = deque([[start,0]])
while q :
    node, time = q.popleft()
    for e,t in graph[0][node]:
        if arrive[e] < time + t :
            arrive[e] = time + t
            q.append([e,time+t])
q = deque([[end,0]])
cnt = 0
visited = [0] * (n+1)
visited[end] = 1
while q :
    node, time = q.popleft()
    for e,t in graph[1][node]:
        if arrive[e] == arrive[node] - t:
            if not visited[e]:
                visited[e] = 1
                cnt += 1
                q.append([e,time+t])
            else :
                cnt += 1
print(arrive[end])
print(cnt)