n = int(input())
left = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    cnt = -1
    for j in range(0,n):
        if ans[j] == 0 :
            cnt += 1
        if cnt==left[i] :
            ans[j] = (i+1)
            break
print(*ans)