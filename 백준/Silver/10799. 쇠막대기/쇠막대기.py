s = input().rstrip()
stack =0
ans = 0
for i in range(len(s)):
    if s[i] == "(" :
        stack += 1
    else :
        stack -= 1
        if s[i-1] == "(" :
            ans += stack
            continue
        ans += 1        
print(ans)