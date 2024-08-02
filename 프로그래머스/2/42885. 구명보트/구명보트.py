from collections import deque
def solution(people, limit):
    
    q = deque(sorted(people))
    last = 0
    ans = 0
    while q :
        last = q.pop()
        
        if q and q[0] + last <= limit :
            q.popleft()
        
        ans += 1
            
    return ans
    
        
            
        
    # 1 3 3 8
    