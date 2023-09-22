n = int(input())
room = [list(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    stack = 0
    for j in range(n):
        if room[i][j] == '.':
            stack  += 1
            if stack == 2:
                cnt += 1
                
                
        else :
            stack = 0
print(cnt, end = ' ')
cnt =0
for i in range(n):
    stack = 0
    for j in range(n):
        if room[j][i] == '.':
            stack  += 1
            if stack == 2:
                cnt += 1
                
                
        else :
            stack = 0
    
print(cnt)