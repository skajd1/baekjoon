for t in range(1, int(input()) + 1):
    n,k = map(int, input().split())
    num = input().strip()
    numList = set()
    numSize = n//4
    for i in range(n):
        tmp = ''
        for j in range(i, i+numSize):
            tmp += num[j%n]
        numList.add('0x'+tmp)
    ans = int(sorted(list(numList),reverse=True)[k-1],16)
    
    
    print("#" + str(t) + " " + str(ans))