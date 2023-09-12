n,m = map(int, input().split())
knows = set(list(map(int, input().split()))[1:])
ans = m
parties = []
for _ in range(m):
    parties.append(set(list(map(int, input().split()))[1:]))
for _ in range(m):
    for party in parties :
        if party & knows :
            knows = knows.union(party)
for party in parties :
    if party & knows :
        ans -= 1
print(ans)