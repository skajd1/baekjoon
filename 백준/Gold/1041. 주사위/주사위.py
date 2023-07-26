n = int(input())
dice = list(map(int, input().split()))
   
# N에 따른 corder, face, edge 케이스 개수 카운트
# 주사위 정보에 따른 케이스 정보 * 카운트 합 

if n == 1 :
    ans = sum(dice) - max(dice)
else :
    corner_num = 4
    edge_num = 4 + 8*(n-2)
    face_num = 5*(n-2)**2 + 4*(n-2)
    corner_arr = []
    edge_arr = []
    tmp = ((1,2),(2,4),(4,3),(3,1))
    for x,y in tmp :
        corner_arr.append(dice[x]+dice[y] + dice[0])
        corner_arr.append(dice[x]+dice[y] + dice[5])
        edge_arr.append(dice[x]+dice[y])
    for i in range(1,5):
        edge_arr.append(dice[0] + dice[i])
        edge_arr.append(dice[5] + dice[i])
    # 4 / 4 0
    # 4 / 4 + 8*(N-2) / (N-2)^2 + 4 + 4
    # 4 / 4 + 8*(N-2) / (N-2)^2 * 5 + (N-2) * 4
    corner = min(corner_arr)
    edge = min(edge_arr)
    face = min(dice)
    ans = corner_num * corner + edge_num*edge + face*face_num


print(ans)
    
