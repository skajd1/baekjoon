import sys
from bisect import bisect_left, bisect_right


def getLength(arr):
    if not arr :
        return 0
    num = len(arr)
    if num == 1 :
        return 1
    # O(n^2)
    # for i in range(1,num):
    #     for j in range(i):
    #         if arr[i] > arr[j] :
    #             dp[i] = max(dp[i], dp[j] + 1)
    
    ## 이분탐색으로 길이 구해보기 -> O(nlogn)
    # 1 5 2 4 5 7
    # 1 2 3 3 3 2 1
    
    tmp = [arr[0]]
    for i in range(1,num):
        if arr[i] > tmp[-1] :
            tmp.append(arr[i])
        else :
            tmp[bisect_left(tmp, arr[i])] = arr[i]
    
    return len(tmp)

            
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# arr 순회하며 arr[i]가 S_k 일 때 를 가정해서 바이토닉 수열의 길이 L_S_k중에 최대 값 고르기.
answer = []

for i in range(n):
    # i 를 기준으로 왼쪽 오른쪽 따로 구하기
    answer.append(getLength(arr[:i]+[arr[i]]) + getLength(list(reversed([arr[i]] + arr[i:]))) -1)
    
print(max(answer))