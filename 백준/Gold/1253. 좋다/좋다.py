n = int(input())
num = list(map(int, input().split()))
num.sort()
ans = 0
for i in range(n):
    left = 0
    right = n-1
    

    while (left<right):
        if left == i :
            left += 1
            continue
        if right == i :
            right -= 1
            continue
        if num[left] + num[right] == num[i] :
            
            ans += 1
            break
        elif num[left] + num[right] < num[i]:
            left += 1
        else:
            right -= 1

print(ans)