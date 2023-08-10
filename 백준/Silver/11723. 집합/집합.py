import sys
input = sys.stdin.readline
s = [0] * 20
for _ in range(int(input())):
    op = input().strip().split()
    if len(op) == 2: n = int(op[1])
    if op[0] == 'add' :
        s[n-1] = 1
    elif op[0] == 'check' :
        print(s[n-1])
    elif op[0] == 'remove' :
        s[n-1] = 0
    elif op[0] == 'toggle' :
        s[n-1] = 0 if s[n-1] else 1
    elif op[0] == 'all' :
        s = [1] * 20
    else :
        s = [0] * 20