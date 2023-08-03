n = int(input())
# 최소 공배수
# GCD -> 최대 공약수
from math import gcd

# 1 0 0 0 1
# 0 1 0 0 3 -> 3 1 0 0 3
# 0 0 1 0 5 -> 15 5 3 0 15
# 0 0 0 1 7 -> 105 35 21 15 15

# 0 0 3 4
# 3 1 0 0 
# 5 0 0 7
ratio = []
for _ in range(n-1):
    a,b,p,q= map(int, input().split())
    GCD = gcd(p,q)
    p = p // GCD
    q = q // GCD
    tmp = []
    for i in range(n):
        if i == a :
            tmp.append(p)
        elif i == b :
            tmp.append(q)
        else :
            tmp.append(0)
    ratio.append(tmp)

tmp = 1
while len(ratio) > 1 :
    check = 0
    for i in range(n):
        if ratio[-1][i] > 0 and ratio[-1 - tmp][i] > 0 :
            p = ratio[-1 - tmp][i]
            q = ratio[-1][i]
            check = 1
            break
    if check :
        for i in range(n):
            ratio[-1 - tmp][i] *=q
            if ratio[-1 - tmp][i] == 0 :
                ratio[-1 - tmp][i] = ratio[-1][i] * p
        tmp = 1
        ratio.pop()
    else :
        tmp += 1
GCD = gcd(ratio[0][0], ratio[0][1])
for i in range(1,n-1):
    GCD = gcd(GCD,gcd(ratio[0][i],ratio[0][i+1]))
for i in range(n):
    ratio[0][i] //= GCD
print(*ratio[0])