import sys

N = int(sys.stdin.readline().rstrip())

deque = []

for i in range(N):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_front':
        # list.insert(i, x): 리스트의 i번째 위치에 x 삽입
        deque.insert(0, int(cmd[1]))
    
    elif cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    
    elif cmd[0] == 'pop_front':
        if deque:
            # list.pop(i): 리스트의 i번째 원소를 리턴하고 삭제
            print(deque.pop(0))
        else: print(-1)
    
    elif cmd[0] == 'pop_back':
        if deque: print(deque.pop())
        else: print(-1)
    
    elif cmd[0] == 'size':
        print(len(deque))
    
    elif cmd[0] == 'empty':
        if deque: print(0)
        else: print(1)
    
    elif cmd[0] == 'front':
        if deque: print(deque[0])
        else: print(-1)
    
    elif cmd[0] == 'back':
        if deque: print(deque[-1])
        else: print(-1)