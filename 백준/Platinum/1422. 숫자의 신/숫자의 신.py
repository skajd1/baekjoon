from functools import cmp_to_key
k,n = map(int,input().split())

def compare(x,y):
    if str(x) + str(y) > str(y) + str(x) :
        return 1
    elif str(x) + str(y) < str(y) + str(x) :
        return -1
    else :
        return 0
num = [int(input()) for _ in range(k)]

num.sort(key = cmp_to_key(compare),reverse = True)
tmp = max(num, key = lambda x : len(str(x)))
for _ in range(n-k):
    num.append(tmp)
num.sort(key = cmp_to_key(compare),reverse = True)

print(*num,sep = "")



