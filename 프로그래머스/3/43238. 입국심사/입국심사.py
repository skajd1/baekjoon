def solution(n, times):
    times.sort()
    left = times[0]
    right = times[-1] * n
    while left<right :
        mid = (left + right) // 2
        tmp = 0
        for time in times:
            tmp += mid // time
        print("mid : ",  mid, "tmp :", tmp)
        if tmp < n :
            left = mid+1
        else :
            right = mid
    return right