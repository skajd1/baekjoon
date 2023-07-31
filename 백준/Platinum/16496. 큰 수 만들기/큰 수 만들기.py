from functools import cmp_to_key
import sys


def compare(x, y):
	if x + y > y + x:
		return 1
	elif y + x > x + y:
		return -1
	return 0


input = sys.stdin.readline
n = int(input())
arr = list(input().strip().split())
arr.sort(key = cmp_to_key(compare),reverse = True)
ans = ""
for x in arr :
	ans+=x

print(int(ans))

