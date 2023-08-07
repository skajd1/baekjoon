from bisect import bisect_right
n = int(input())
cweight = list(map(int, input().split()))
cweight.sort()
m = int(input())
bweight = list(map(int, input().split()))
bweight.sort()
ans = 0
check = []


if cweight[-1] < bweight[-1] :
    print(-1)
else :
    check = list((map(lambda x : bisect_right(bweight,x),cweight)))

    while check[-1] != 0 :
        for i in range(len(check)):
            if check[i] > 0 :
                check = list(map(lambda x : x-1 if x >= check[i] else x, check))
        ans += 1
        
    print(ans)