paper = [list(map(int, input().split())) for _ in range(10)]
cnt = [5] * 5
ans = 1e9
flag = False
s = sum([sum(paper[i]) for i in range(10)])

# 현재 사이즈로 현재 위치에 종이를 둘 수 있는지 체크하는 함수
def check(size,x,y):
    for i in range(x, size+ x):
        for j in range(y, size + y):
            if not paper[i][j]  : return False
    return True
# 현재 위치에 현재 사이즈만큼 visit 처리해주는 함수
def visit(size,x,y):
    global paper
    for i in range(x,size + x):
        for j in range(y,size + y):
            paper[i][j] = 0
def unVisit(size,x,y):
    global paper
    for i in range(x,size + x):
        for j in range(y,size + y):
            paper[i][j] = 1

# 지금 사이즈 몇개 붙일 수 있는 지 계산 하고
# 현재 ans보다 커지면 return 
def dfs(x,y,now):
    global ans,cnt,flag
    if x >= 10 :
        ans = min(now,ans)
        flag = True
        return
    if y >= 10 :
        dfs(x+1,0,now)
        return
    if paper[x][y]:
        for size in range(1,6):
            if cnt[size-1] > 0 and x+size <= 10 and y+size <= 10 :
                if check(size,x,y):
                    visit(size,x,y)
                    cnt[size-1] -= 1
                    dfs(x,y+size,now+1)
                    unVisit(size,x,y)
                    cnt[size-1] += 1
                else : break
    else : dfs(x,y+1,now)
dfs(0,0,0)

# 완성 못하는 경우 -> 완성했을 때 flag 처리해서 출력할 때 조건 분기 @@@
print(ans) if flag else print(-1)