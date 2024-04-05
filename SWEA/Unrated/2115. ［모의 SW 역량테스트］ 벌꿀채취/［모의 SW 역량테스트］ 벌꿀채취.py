from itertools import combinations

def getSqureSum(arr):
    S = 0
    # c 이하의 최대 부분수열의 합 리턴
    for x in [combinations(arr, i) for i in range(1, m+1)]:
        for part in x :
            if sum(part) <= c :
                # print(list(part))
                S = max(S, sum([X**2 for X in part]))
    
    return S
    
    
for t in range(1,int(input()) + 1) :
    ans = 0
    n,m,c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    maxHoney = [[0] * n for _ in range(n)]
    
    for i in range(0, n):
        for j in range(0, n-m+1) :
            maxHoney[i][j] = getSqureSum(board[i][j:j+m])
    for i in range(n):
        for j in range(n):
            h1 = maxHoney[i][j]
            if not h1 : continue
            for k in range(i,n):
                for l in range(0,n):
                    if k == i :
                        if j<=l<j+m or l+m > n or l < j : continue
                    h2 = maxHoney[k][l]
                    ans = max(ans, h1+h2)


    print("#" + str(t) + " " + str(ans))
    