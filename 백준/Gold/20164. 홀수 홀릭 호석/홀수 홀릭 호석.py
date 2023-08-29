import sys

n = sys.stdin.readline().rstrip()
minVal = float('inf')
maxVal = 0

def check_odd(s) :
    cnt = 0
    for i in s :
        if int(i) % 2 == 1 :
            cnt += 1
    return cnt

def dfs(s, cnt) :
    global minVal, maxVal

    cnt = cnt + check_odd(s)
    if len(s) == 1 :
        minVal = min(minVal, cnt)
        maxVal = max(maxVal, cnt)
    elif len(s) == 2 :
        temp = int(s) // 10 + int(s) % 10
        dfs(str(temp), cnt)
    else :
        for i in range(1,len(s)) :
            for j in range(i+1, len(s)) :
                temp = int(s[:i]) + int(s[i:j]) + int(s[j:])
                dfs(str(temp),cnt)
dfs(n,0)
print(minVal, maxVal)