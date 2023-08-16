n = int(input())
img = [list(input().strip()) for _ in range(n)]
# 쿼드 트리
def checkZero(size,x,y):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if img[i][j] != '0':
                return False
    return True
def checkOne(size,x,y):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if img[i][j] != '1':
                return False
    return True
ans = ""
def quadTree(size,x,y):
    global ans
    if checkZero(size,x,y):
        ans += "0"
        return
    elif checkOne(size,x,y):
        ans += "1"
        return
    elif size == 1:
        ans += img[x][y]
        return
    else:
        ans += "("
        quadTree(size//2,x,y)
        quadTree(size//2,x,y+size//2)
        quadTree(size//2,x+size//2,y)
        quadTree(size//2,x+size//2,y+size//2)
        ans += ")"
quadTree(n,0,0)
print(ans)
