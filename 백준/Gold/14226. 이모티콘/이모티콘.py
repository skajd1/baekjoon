from collections import deque
s = int(input())

q = deque()
q.append(([1,0,0]))
visited = [[0] *1001 for _ in range(1001)]
visited[1][0] = 1

while q :
    now,time,clip = q.popleft()
    if now == s :
        print(time)
        break
    if clip and now + clip <= 1000 and not visited[now+clip][clip]:
        visited[now+clip][clip] = 1
        q.append([now + clip, time + 1, clip])
    if now > 0 and now < 1001 and not visited[now][now]:
        visited[now][now] = 1
        q.append([now, time + 1, now])
    if now > 0 and not visited[now-1][clip]:
        visited[now-1][clip] = 1
        q.append([now - 1, time + 1, clip])
        