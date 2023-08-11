string = list(input().strip())
b = input().strip()
s = []

for x in string:
    s.append(x)
    if s[-1] == b[-1] :
        tmp = 0
        while True :
            if tmp == len(b) : break
            if len(s) > tmp and s[-1-tmp] == b[-1-tmp] :
                tmp += 1
            else :
                tmp = 0
                break
        for _ in range(tmp):
            s.pop()    

if s: print(*s,sep='')
else : print("FRULA")