from collections import deque
def solution(cards):
    ans = []
    visited = [0] * len(cards)
    for i in range(len(cards)):
        if visited[i]: continue
        tmp = []
        q = deque([i])
        visited[i] = 1
        while q:
            x = q.popleft()
            tmp.append(x)
            if not visited[cards[x]-1] :
                visited[cards[x]-1] = 1
                q.append(cards[x]-1)
        ans.append(len(tmp))
    ans.sort()
    return ans[-1] * ans[-2] if len(ans) >= 2 else 0