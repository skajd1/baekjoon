a,b,c = map(int, input().split())

def func(a,b,c):
    if b == 1:
        return a % c
    else:
        temp = func(a,b//2,c)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c
print(func(a,b,c))