t = int(input())
for _ in range(t) :
    n,m = map(int, input().split())
    bookRange = [list(map(int, input().split())) for _ in range(m)]
    visited = [0] * (n+1)
    ans = 0
    bookRange.sort(key = lambda x : (x[1]))

    for x,y in bookRange:
        for i in range(x,y+1):

            if not visited[i] :
                visited[i] = 1
                ans +=1
                break
    print(ans)