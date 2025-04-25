from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    ans = 0
    right = 0
    while q :
        right = q.pop()
        if q and q[0] + right <= limit:
            q.popleft()
        ans += 1
    return ans




    