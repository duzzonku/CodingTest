#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15686                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15686                          #+#        #+#      #+#     #
#    Solved: 2026/03/06 15:58:14 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append((i, j))

        if board[i][j] == 2:
            chickens.append((i, j))


min_city_dist = 99999
selected_chickens = []

def dfs(start, cnt):
    global min_city_dist

    if cnt == M:
        city_dist = 0

        for house_r, house_c in houses:
            min_dist = float('inf')

            for chicken_r, chinken_c in selected_chickens:
                dist = abs(chicken_r - house_r) + abs(chinken_c - house_c)
                
                if dist < min_dist:
                    min_dist = dist

            city_dist += min_dist

        if city_dist < min_city_dist:
            min_city_dist = city_dist
        
        return

    for i in range(start, len(chickens)):
        selected_chickens.append(chickens[i])
        dfs( i + 1, cnt + 1)
        selected_chickens.pop()

dfs(0, 0)

print(min_city_dist)