arr = [int(input()) for _ in range(9)]
visited= [0] * 9
arr.sort()
def comb(cnt):
    global ans
    if cnt == 9 :
        if sum([arr[i] for i in range(9) if visited[i]]) == 100 and sum(visited) == 7 :
            for i in range(9):
                if visited[i] : print(arr[i])
            exit(0)
        return
    
    visited[cnt] = 1
    comb(cnt+1)
    visited[cnt] = 0
    comb(cnt+1)
comb(0)