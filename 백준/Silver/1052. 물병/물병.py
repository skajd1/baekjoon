n, k =map(int, input().split())
num = n
ans = 0
while bin(n).count('1') > k :
    n += 1
print(n-num)
