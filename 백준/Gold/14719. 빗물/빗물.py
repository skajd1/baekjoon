h,w = map(int, input().split())
height = list(map(int, input().split()))

# 최고 높이가 1개면 -= 1 해주기
# 2개 이상이면 가장 왼쪽과 가장 오른쪽 인덱스 사이에 있는 모든 height에 대해서
# height < 최고 높이 이면 ans += 1
# 최고높이인 모든 블럭 -= 1
# ... 반복

# 모든 블럭의height가 0이되면 break

# answer 출력

# -> 500 * 500 번
ans = 0
while(True):
    
    M = max(height)
    if M == 0 : break
    left = 0
    right = w-1
    for i in range(0,w):
        if height[i] == M :
            left = i
            break
    for i in range(w-1,-1,-1):
        if height[i] == M :
            right = i
            break
    if left == right :
        height[left] -= 1
        continue
    else :
        for i in range(left,right+1):
            if height[i] < M :
                ans += 1
            if height[i] == M :
                height[i] -= 1

print(ans)