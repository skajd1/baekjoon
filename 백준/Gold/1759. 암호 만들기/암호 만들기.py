import sys
input = sys.stdin.readline
l,c = map(int, input().split())
s = list(input().split())
s.sort()

aeiou = ['a','e','i','o','u']
arr = []

def f(x):
	a = 0 # 자음
	b = 0 # 모음

	if len(arr) == l:
		for ss in arr:
			if ss in aeiou:
				b +=1
			else:
				a +=1
		if not (a>=2 and b>=1) :
			return
		print(*arr,sep ='')
		return

	for i in range(x,c):
		if s[i] not in arr:
			arr.append(s[i])
			if s[i] in aeiou:
				b += 1
			else :
				a += 1
			f(i+1)
			arr.pop()

f(0)