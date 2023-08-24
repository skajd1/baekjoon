parents = []
def find(a):
    if parents[a] == a : return a
    parents[a] = find(parents[a])
    return parents[a]
def union(a,b):
    A = find(a)
    B = find(b)
    if A==B : return False
    parents[B] = A
    return True
while(1):
    m,n =map(int, input().split())
    if m == 0 and n == 0 : break
    
    ans = 0
    roadInfo = []
    s = 0
    parents = [i for i in range(m)]
    for _ in range(n):
        x,y,z = map(int, input().split())
        roadInfo.append([x,y,z])
        s += z
    roadInfo.sort(key = lambda x : x[2])
    tmp = []
    for x,y,z in roadInfo :
        if(union(x,y)) : ans += z
    print(s-ans)