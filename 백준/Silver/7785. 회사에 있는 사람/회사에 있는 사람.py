d = dict()
n = int(input())
for x, y in [input().split() for _ in range(n)]:
    d[x] = d.get(x,0) +1 if y == 'enter' else d.get(x,0) -1
print(*sorted([x for x in d if d[x] > 0], reverse=True), sep='\n')