def getHouseinArea(k,x,y):
    if k==1:
        if board[x][y] :
            dp[x][y][k] = 1
            return 1
        else : return 0
        
    # k-1일 때의 영역에서 가장자리를 따라 검사하기

    cnt = 0
    for i in range(k-1) :
        x1 = x -(k-1) + i
        y1 = y + i
        x2 = x + i
        y2 = y + (k-1) - i
        x3 = x + (k-1) - i
        y3 = y - i
        x4 = x - i
        y4 = y - (k-1) + i
        if chkRange(x1,y1) and board[x1][y1] : cnt += 1
        if chkRange(x2,y2) and board[x2][y2] : cnt += 1
        if chkRange(x3,y3) and board[x3][y3] : cnt += 1
        if chkRange(x4,y4) and board[x4][y4] : cnt += 1
    
    cnt += dp[x][y][k-1]
    dp[x][y][k] = cnt
            
    return cnt

for t in range(1, int(input()) + 1):
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_k = n*2
    HouseCountForEachK = [0] * (max_k + 1) 
    dp = [[[0] * (max_k+1) for _ in range(n)] for _ in range(n)]
    chkRange = lambda x,y : True if 0<=x<n and 0<=y< n else False
    for i in range(n):
        for j in range(n):        
            for k in range(1,max_k +1) :
                HouseCountForEachK[k] = max(HouseCountForEachK[k],getHouseinArea(k,i,j))
    ans = 0
    for k in range(1,max_k+1) :
        if m*HouseCountForEachK[k] - (k**2 + (k-1)**2) >= 0 :
            ans = max(ans, HouseCountForEachK[k])
    # print(HouseCountForEachK)
    # print(dp[0][0])
    print("#" + str(t) + " " + str(ans))