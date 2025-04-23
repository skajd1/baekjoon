def solution(citations):
    ans = len(citations)
    for i,c in enumerate(sorted(citations)):
        if ans > c : ans -= 1
        else: return ans
    return ans
        
