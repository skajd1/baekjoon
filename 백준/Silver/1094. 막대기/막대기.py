x = int(input())
ans = 0
while x > 0 :
    i = 1
    while 2 ** i <= x :
        i+=1
    x -= 2**(i-1)
    ans += 1
print(ans)