from collections import deque
def solution(sequence, k):
    answer = []
    index = len(sequence) -1
    now = sequence[index]
    tmp = deque([index])
    while True:
        if now < k :
            index -= 1
            now += sequence[index]
            tmp.append(index)
        elif now > k :
            now -= sequence[tmp.popleft()]
        else :
            while index > 0 and sequence[index-1] == sequence[tmp[0]] :
                tmp.popleft()
                index -= 1
                tmp.append(index)
            
            answer = [tmp[-1],tmp[0]]
            break        
        
    
    return answer