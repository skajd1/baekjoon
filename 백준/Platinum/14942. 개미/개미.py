from collections import deque
n = int(input())
energy = [0] + [int(input()) for _ in range(n)]
graph = [[] for _ in range(n+1)]
for s,e,d in list(map(int, input().split()) for _ in range(n-1)):
    graph[s].append((e,d))
    graph[e].append((s,d))
distance = [float('inf')] * (n+1) # i번째 방에서 1번 방까지의 거리
distance[1] = 0
rooms = [i for i in range(n+1)] 
parents = [i for i in range(n+1)]

#### 노드가 n개이고 간선이 n-1개이므로 스패닝 트리가 됨 ####
# 트리의 특성상 depth가 낮을 수록 1에 가까운 방이 된다. (다시 depth가 커지는 방향으로는 이동 x)

# 방과 방 사이 거리는 두 개의 방을 연결하는 경로를 구성하는 굴의 길이의 합
# 이동 시 굴의 길이 만큼 에너지 소모
# 각 개미가 갈 수 있는 방들 중 1에 가까운 방을 bfs 돌면서 계속 업데이트
# 1에 갈 수 있냐 없냐는 판단이 되는데 가장 가까운 방은 어떻게 찾지

def getDist():
    q = deque([[1,0]])
    visited = [0] * (n+1)
    visited[1] = 1
    while q :
        # 현재 방, 현재 방까지 드는 에너지
        
        node,dist = q.popleft()
        if energy[node] >= dist:
            rooms[node] = 1
        else :
            # rooms[node]를 가능한 1과 가장 가까운 노드로 업데이트
            p = parents[node]
            while True:
                if energy[node] >= dist-distance[p]:
                    rooms[node] = p
                    p = parents[p]
                else :
                    break
        
        for next,next_dist in graph[node] :
            if rooms[next] == 1 or visited[next]:
                continue
            parents[next] = node
            distance[next] = dist + next_dist
            visited[next] = 1
            q.append([next,distance[next]])
            
getDist()
print(*rooms[1:],sep = '\n')