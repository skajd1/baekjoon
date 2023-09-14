n=int(input())
ramen = list(map(int,input().split())) + [0,0]
ans = 0
def buy3(idx):
    global ans
    m = min(ramen[idx],ramen[idx+1],ramen[idx+2])
    ans += m * 7
    ramen[idx] -= m
    ramen[idx+1] -= m
    ramen[idx+2] -= m
def buy2(idx):
    global ans
    m = min(ramen[idx],ramen[idx+1])
    ans += m * 5
    ramen[idx] -= m
    ramen[idx+1] -= m
def buy1(idx):
    global ans
    ans += ramen[idx] * 3
    ramen[idx] = 0
for i in range(n):
    if ramen[i+1] > ramen[i+2]:
        m = min(ramen[i],ramen[i+1]-ramen[i+2])
        ans += m * 5
        ramen[i] -= m
        ramen[i+1] -= m
        buy3(i)
    else:
        buy3(i)
        buy2(i)
    buy1(i)

print(ans)