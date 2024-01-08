from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] * (n+1)
    depth = [0] * (n+1)
    tree = [[] for _ in range(n+1)]
    for a,b in [map(int, input().split()) for _ in range(n-1)]:
        parent[b] = a
        tree[a].append(b)
    visited = [0] * (n+1)
    for i in range(1,n+1):
        if not parent[i] :
            root = i
            q = deque()
            q.append([root,0])
            depth[root] = 0
            while q :
                node, d = q.popleft()
                depth[node] = d
                for next_node in tree[node]:
                    q.append([next_node, d+1])
            
            break
    A,B = map(int, input().split())
    # 1. 둘 중 하나가 나머지 하나의 부모면 그거 출력
    # 2. 부모가 같으면 그거 출력
    # 3. 다르면 depth가 같은지 보고, depth가 큰 쪽을 내려준다.
    
    while depth[A] != depth[B] :
        if depth[A] > depth[B] :
            A = parent[A]
        else :
            B = parent[B]
    while A != B :
        A = parent[A]
        B = parent[B]
    print(A)
    