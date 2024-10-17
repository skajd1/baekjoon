def solution(scores):
    answer = 0
    tmp = sorted(scores[1:], key = lambda x : (-x[0],x[1]))
    if not tmp : return 1
    threshold = tmp[0][1]
    incentive = []
    left = tmp[0][0]
    for l,r in tmp :
        if l > scores[0][0] and r > scores[0][1] : return -1
        if threshold <= r : 
            incentive.append(l+r)
            threshold = r
    incentive.sort(reverse=True)

    for i,x in enumerate(incentive):
        if scores[0][0] + scores[0][1] >= x:
            return i+1
    return len(incentive) + 1


