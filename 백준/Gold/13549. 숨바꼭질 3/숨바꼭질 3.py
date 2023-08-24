n,k = map(int, input().split())

from collections import deque

visited = [0] * 100001
visited[n] = 1
q = deque([[n,0]])
while q:
    now, t = q.popleft()
    if now == k :
        print(t)
        break

    if now*2 <= 100000 and not visited[now*2]:
        q.append([now*2, t])
        visited[now*2] = 1
    if now -1 >= 0 and not visited[now-1]:
        q.append([now-1,t+1])
        visited[now-1] = 1
    if now + 1 <=100000 and not visited[now+1]:
        q.append([now+1, t+1])
        visited[now+1] = 1