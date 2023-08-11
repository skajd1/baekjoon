import sys
input = sys.stdin.readline
n,m = map(int, input().split())
words = set()
s = {}
for _ in range(n):
    if len(x := input().strip()) >= m :
        s[x] = s.get(x,0) + 1
        words.add(x)
print(*sorted(list(words),key = lambda x : (-s[x],-len(x),x)),sep="\n")