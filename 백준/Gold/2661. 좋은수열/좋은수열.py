n = int(input())
ans = []
# 파라미터로 받은 arr이 좋은 수열인지 판단하는 함수
def check(arr):
    tmp = 1
    for i in range(len(arr)-1, -1, -1):
        
        if(arr[i:] == arr[i-tmp:i]):
            return False
        tmp += 1
    return True
def dfs(cnt):
    # cnt 는 ans의 길이
    if cnt == n :
        print(*ans,sep="")
        exit(0)
    # 1부터 ans에 넣어보면서 이전 부분수열과 겹치는지 체크
    for i in range(1,4):
        if(check(ans+[i])) :
            ans.append(i)
            dfs(cnt+1)
            ans.pop()
dfs(0)