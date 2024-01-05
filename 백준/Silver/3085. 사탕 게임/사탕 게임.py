n = int(input())
board = [list(input().strip()) for _ in range(n)]
ans = 1
# n <= 50

def findMaxLength(b):
    res = 1
    #행
    for i in range(n):
        cnt1 = 1
        cnt2 = 1
        for j in range(1,n):
            if b[i][j] == b[i][j-1] : cnt1 += 1
            else : cnt1 = 1
            if b[j][i] == b[j-1][i] : cnt2 += 1
            else : cnt2 = 1
            res = max(res,cnt1,cnt2)
    
    return res

for i in range(n):
    for j in range(1,n):
        if board[i][j] != board[i][j-1] :
            board[i][j],board[i][j-1] = board[i][j-1],board[i][j]
            ans = max(ans,findMaxLength(board))
            board[i][j],board[i][j-1] = board[i][j-1],board[i][j]
        
        if board[j][i] != board[j-1][i] :
            board[j][i],board[j-1][i] = board[j-1][i],board[j][i]
            ans = max(ans,findMaxLength(board))
            board[j][i],board[j-1][i] = board[j-1][i],board[j][i]
        
print(ans)