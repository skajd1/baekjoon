from collections import defaultdict


def f(s):
	d = defaultdict(int)
	cnt = 0

	odd_s = ''
	answer_left = ''
	answer_right = ''
	if len(s) == 1:
		print(s)
		return
	else:
		for ss in sorted(s):
			d[ss] += 1
		for x in d:
			answer_left = answer_left + x * (d[x] // 2)
			answer_right = x * (d[x] // 2) + answer_right
			if d[x] % 2 == 1:
				cnt += 1
				if cnt == 2:
					print("I'm Sorry Hansoo")
					return
				odd_s = x
		answer = answer_left + odd_s + answer_right
	print(answer)


f(input())