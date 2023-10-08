from collections import deque
class Client:
    def __init__(self, x, y, dest_x, dest_y):
        self.x = x
        self.y = y
        self.dest_x = dest_x
        self.dest_y = dest_y
    
n,m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

now = list(map(int, input().split()))
clients = []
for _ in range(m):
    clients.append(Client(*map(int, input().split())))
clientNum = -1
def getClient():
    global now,fuel,clientNum
    candidate = []
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append(now +[fuel])
    visited[now[0]-1][now[1]-1] = 1
    while q :
        x,y,left = q.popleft()
        for i,client in enumerate(clients):
            if client.x == x and client.y == y:
                if not candidate:
                    candidate.append([x,y,left,i])
                elif candidate and candidate[-1][2] >= left :
                    candidate.append([x,y,left,i])
        if left == 0:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx-1<n and 0<=ny-1<n and visited[nx-1][ny-1] == 0 and board[nx-1][ny-1] != 1:
                q.append([nx,ny,left-1])
                visited[nx-1][ny-1] = 1
    if candidate:
        candidate.sort(key = lambda x : (-x[2],x[0],x[1]))
        now = [candidate[0][0],candidate[0][1]]
        clientNum = candidate[0][3]
        fuel = candidate[0][2]
        return True
    return False
        
            
def goDest():
    global now,fuel
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append(now +[0,fuel])
    visited[now[0]-1][now[1]-1] = 1
    while q:
        x,y,dist,left = q.popleft()
        if x == clients[clientNum].dest_x and y == clients[clientNum].dest_y:
            now = [x,y]
            fuel = left + 2*dist
            return True
        if left == 0 :
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx-1<n and 0<=ny-1<n and visited[nx-1][ny-1] == 0 and board[nx-1][ny-1] != 1:
                q.append([nx,ny,dist+1,left-1])
                visited[nx-1][ny-1] = 1
    return False


while True:
    if getClient() :
        if goDest():
            clients.pop(clientNum)            
        else:
            fuel = -1
            break
    else :
        fuel = -1
        break
    if len(clients) == 0:
        break
print(fuel)