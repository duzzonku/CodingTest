#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2026/02/26 16:33:30 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

N = int(input())
map = [list(map(int, input())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    cnt = 1

    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]
            
            if 0 <= nr < N and 0 <= nc < N:
                if map[nr][nc] == 1:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        cnt += 1
    return cnt


total_cnt = []

for row in range(N):
    for col in range(N):
        if map[row][col] == 1:
            if not visited[row][col]:
                house_count = bfs(row, col)
                total_cnt.append(house_count)

total_cnt.sort()

print(len(total_cnt))
for i in range(len(total_cnt)):
    print(total_cnt[i])