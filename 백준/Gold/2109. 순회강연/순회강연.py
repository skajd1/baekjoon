# 가장 많은 돈을 벌게.
# 우선 순위 큐

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
q = []
ans = 0
arr = []
# d가 now보다 작은 것 중에서 제일 큰 것만 취하기
# d가 같으면 p가 큰거 먹기
# d가 작아도 p가 크면 먹기
for p,d in [map(int, input().split()) for _ in range(n)]:
    arr.append(((p,d)))

arr.sort(key = lambda x : (x[1]))
now = 10000

while now >= 1:
    while arr and arr[-1][1] >= now:
        heappush(q, -arr.pop()[0])
    if q:
        ans -= heappop(q)
    now -= 1

print(ans)






