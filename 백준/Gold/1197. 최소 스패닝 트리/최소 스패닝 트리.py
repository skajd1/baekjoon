v,e = map(int, input().split())
edge =sorted([list(map(int, input().split())) for _ in range(e)],key = lambda x : x[2])
parents =[i for i in range(0,v+1)]
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
ans = 0
for s,e,w in edge :
    if(union(s,e)) : ans += w
print(ans)