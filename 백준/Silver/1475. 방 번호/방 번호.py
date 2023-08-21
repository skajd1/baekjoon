n = list(input().strip())
num = [0] * 10
ans = 0
def func():
    global num,ans,n
    num = list(map(lambda x : x+1,num))
while n :
    x = int(n[-1])    
    if not num[x] :
        if x == 9 :
            if num[6] :
                num[6] -= 1
                n.pop() 
                continue
        elif x == 6 :
            if num[9] :
                num[9] -= 1
                n.pop() 
                continue
        func()
        ans += 1
    else :
        n.pop() 
        num[x]-=1
print(ans)