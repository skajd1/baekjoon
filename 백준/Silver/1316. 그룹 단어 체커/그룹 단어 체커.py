n = int(input())
ans = n
words = [list(input().strip()) for _ in range(n)]
for word in words:
    used = [0] * 26
    i = 0
    while i< len(word):
        if not used[ord(word[i]) - ord('a')] :
            used[ord(word[i]) - ord('a')] = 1
            while (i+1) < len(word) and word[i] == word[i+1] :
                i+=1
        else :
            ans -= 1
            break
        i+=1
print(ans)