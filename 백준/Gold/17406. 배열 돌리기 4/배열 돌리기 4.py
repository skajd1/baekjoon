n,m,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rotation = [list(map(int, input().split())) for _ in range(k)]
order = []
visited = [0] * k
ans = float('inf')
def copy():
    tmp = [arr[i][:] for i in range(n)]
    return tmp
def rotate(array, rr):
    r,c,s = rr
    r -= 1
    c -= 1
    x,y = r-s, c-s
    xx,yy = r+s, c+s
    # x,y부터 xx,yy까지 시계방향으로 1칸씩 이동
    # 제일 바깥 링부터 회전
    cnt = 0
    while(cnt < s):
        nx = x + cnt
        ny = y + cnt
        nxx = xx - cnt
        nyy = yy - cnt

        tmp = array[nx][ny]
        # 왼
        for i in range(nx, nxx):
            array[i][ny] = array[i+1][ny]        
        # 아래
        for i in range(ny, nyy):
            array[nxx][i] = array[nxx][i+1]
        # 오른
        for i in range(nxx, nx-1, -1):
            array[i][nyy] = array[i-1][nyy]
        # 위
        for i in range(nyy, ny+1,-1):
            array[nx][i] = array[nx][i-1]
        array[nx][ny+1] = tmp
        cnt += 1

    
def dfs(cnt):
    global ans
    if cnt == k :
        copied = copy()
        for o in order:
            rotate(copied,rotation[o])
        ans = min(ans, min([sum(s) for s in copied]))        
        return
        
    for i in range(k):
        if not visited[i]:
            order.append(i)
            visited[i] = 1
            dfs(cnt+1)
            order.pop()
            visited[i] = 0

dfs(0)
print(ans)