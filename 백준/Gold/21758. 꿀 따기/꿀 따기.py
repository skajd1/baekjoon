import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

s = sum(arr)
acc = [arr[0]]
for i in range(1,n):
    acc.append(arr[i] + acc[-1])
    
ans = 0

# n은 10^5

# 벌통 벌벌
# 무조건 벌 1마리는 오른쪽 끝, 벌통은 왼쪽 끝에 있어야 최대치 뽑을 수 있다.
# 벌 1마리의 위치를 움직이면서 별꿀 양 구하기
for i in range(1,n-1):
    ans = max(ans, (acc[n-2] - arr[i] + acc[i-1]))

# 벌 벌통 벌
for i in range(1,n-1):
    ans = max(ans, s - arr[0] - arr[n-1] + arr[i])
    
# 벌 벌 벌통
# 별 1마리는 왼쪽 끝, 별통은 오른쪽 끝
for i in range(1,n-1):
    ans = max(ans, (s - arr[0] - arr[i] + s - acc[i]))
    
print(ans)