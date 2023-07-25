from bisect import bisect_left
from collections import deque
n,m = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

ans = 0
zero = bisect_left(loc,0)

left = deque(loc[:zero])
right = deque(loc[zero:])
# 끝 값의 절대값이 큰 쪽을 먼저 더해주기 
# 그 쪽 원소가 2개이상이면 2개 pop 해주고 제일 끝값 * 1 만큼 더하기

# 길이 긴 순으로 왕복 -> 제일 끝값 *2 만큼 더하고 pop 2개 (원소 1개면 1개만)
# left만 있는 경우 / 둘 다 있는 경우 / right만 있는 경우 

def move(left,right):
    global ans
    # while left or right:
    #     pass
    if left and right :
        if abs(left[0]) >= abs(right[-1]):
            ans += 2*abs(left.popleft())
            for _ in range(m-1):
                if left :
                    left.popleft()
        else :
            ans += 2*abs(right.pop())
            for _ in range(m-1):
                if right :
                    right.pop()
    elif not left :
        ans += 2*right.pop()
        for _ in range(m-1):
            if right : right.pop()
    elif not right:
        ans += 2*abs(left.popleft())
        for _ in range(m-1):
            if left : left.popleft()




if left and right :
    if abs(left[0]) >= abs(right[-1]):
        ans += abs(left.popleft())
        for _ in range(m-1):
            if left :
                left.popleft()
    else :
        ans += abs(right.pop())
        for _ in range(m-1):
            if right :
                right.pop()
elif not left :
    ans += right.pop()
    for _ in range(m-1):
        if right : right.pop()
    
elif not right:
    ans += abs(left.popleft())
    for _ in range(m-1):
        if left : left.popleft()

while left or right:
    move(left,right)


print(ans)
