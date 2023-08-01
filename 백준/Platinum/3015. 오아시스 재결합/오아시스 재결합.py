n = int(input())
height =[int(input()) for _ in range(n)]
ans = 0
# O(NlogN) 이하로 ( N ~ 500,000 )
# n번 순회
# 자신보다 작은 값이면 스택에 넣고, 자신의 value += 1
# 
# 자신보다 큰 값을 만나면 지금까지의 value를 다음 값에 전달, 스택 빠져나오기 
# 스택 빠져나오면서 저장된 value 전부 ans에 더하기

stack = []

for h in height :

    while stack and stack[-1][0] < h :
        ans += stack.pop()[1]
    if not stack:
        stack.append([h,1])
        continue
    
    
    if stack[-1][0] == h :
        cnt = stack.pop()[1]
        ans += cnt
        if stack : ans += 1
        stack.append([h,cnt+1])
    else :
        stack.append([h,1])
        ans += 1
    

print(ans)