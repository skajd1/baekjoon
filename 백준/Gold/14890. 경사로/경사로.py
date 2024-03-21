n,l = map(int,input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for road in roads:
	cnt = 1
	flag = False
	can = True
	tmp = []
	for i in range(0, n):
		if l == 1 :
			flag = True
		if i == 0 :
			continue
		if i in tmp :
			cnt = 0
			continue 
		if road[i] == road[i-1] :
			cnt += 1
			if cnt == l :
				flag = True
				cnt = 0
		elif road[i] == road[i-1] + 1 : 
			if flag :
				for j in range(l):
					if (i-1-j) in tmp :
						can = False
						break
					tmp.append(i-1-j)
			else :
				can = False
				break
			flag = False
			cnt = 1
	
		elif road[i] == road[i-1] - 1 : # 1칸 내려갈 때
			cnt2 = 0
			for k in range(l):
				if i+k < n and road[i] == road[i+k] :
					cnt2 += 1
			if cnt2 == l :
				for x in range(l):
					tmp.append(i+x)
			else :
				can = False
				break
		else :
			can = False
	if can : 
		ans += 1
for a in range(n):
	cnt = 1
	flag = False
	can = True
	tmp = []
	for b in range(0, n):
		if l == 1 :
			flag = True
		if b == 0 :
			continue
		if b in tmp :
			cnt = 0
			continue 
		if roads[b][a] == roads[b-1][a] :
			cnt += 1
			if cnt == l :
				flag = True
				cnt = 0
		elif roads[b][a] == roads[b-1][a] + 1 : 
			if flag :
				for c in range(l):
					if (b-1-c) in tmp :
						can = False
						break
					tmp.append(b-1-c)
			else :
				can = False
				break
			flag = False
			cnt = 1
	
		elif roads[b][a] == roads[b-1][a] - 1 : # 1칸 내려갈 때
			cnt2 = 0
			for d in range(l):
				if b+d < n and roads[b][a] == roads[b+d][a] :
					cnt2 += 1
			if cnt2 == l :
				for y in range(l):
					tmp.append(b+y)
			else :
				can = False
				break
		else :
			can = False
	if can : 
		ans += 1
print(ans)		
		
		