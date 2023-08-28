def find(x):
    if parents[x] == x :
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    X = find(x)
    Y = find(y)
    if(X==Y):
        return False
    parents[Y] = X
    return True


n=int(input())
m = int(input())
ans = 'YES'
parents = [i for i in range(n+1)]
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if(graph[i][j]):
            union(i+1,j+1)
for i in range(m-1):
    if(find(plan[i]) != find(plan[i+1])):
        ans = 'NO'
        break
print(ans)