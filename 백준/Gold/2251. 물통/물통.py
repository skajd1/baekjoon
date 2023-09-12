a,b,c = map(int, input().split())
waters = [0] * (c+1)
waters[c] = 1
visited = [[0] * (b+1) for _ in range(a+1)]
def bfs():
    from collections import deque
    q = deque([[0,0,c]])
    while q :
        x,y,z = q.popleft()
        if visited[x][y] : continue
        visited[x][y] = 1
        if x == 0 :
            waters[z] = 1
        # 6가지 경우의수
        # a -> b
        if x+y > b :
            q.append([x+y-b,b,z])
        else :
            q.append([0,x+y,z])
        # a -> c
        if x+z > c :
            q.append([x+z-c,y,c])
        else :
            q.append([0,y,x+z])
        # b -> a
        if x+y > a :
            q.append([a,x+y-a,z])
        else:
            q.append([x+y,0,z])
        # b -> c
        if y+z > c :
            q.append([x,y+z-c,c])
        else :
            q.append([x,0,y+z])
        # c -> a
        if x+z > a:
            q.append([a,y,x+z-a])
        else :
            q.append([x+z,y,0])
        # c -> b
        if y+z > b :
            q.append([x,b,y+z-b])
        else :
            q.append([x,y+z,0])
            


        

bfs()
for i in range(len(waters)):
    if waters[i]:
        print(i, end=' ')