from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
lis = [arr[0]]
for i in range(1,n):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        lis[bisect_left(lis, arr[i])] = arr[i]
print(len(lis))