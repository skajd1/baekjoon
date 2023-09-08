import sys
input = sys.stdin.readline
n, k = map(int, input().split())
h = list(map(int, input().split()))

# 1 3 5 6 10
# diff : 2 2 1 4
diff = []
for i in range(n-1):
    diff.append(h[i+1] - h[i])
diff.sort(reverse=True)
print(sum(diff[k-1:]))