#그리디, 힙큐
from heapq import heappop, heappush
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x : (x[0],-x[1]))
q =  []
answer = 0
day = arr[-1][0]
while day>=1 :
    while arr and arr[-1][0] == day:
        heappush(q,-arr.pop()[1])
    if q :
        answer += -heappop(q)
    day -= 1
print(answer)

# arr을 정렬 후, 거꾸로 순회하면서 현재 낼 수 있는 가장 큰 점수 (힙큐 이용)를 answer에 더해주기

 