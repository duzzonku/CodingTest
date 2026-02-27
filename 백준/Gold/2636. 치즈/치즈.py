#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2636                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2636                           #+#        #+#      #+#     #
#    Solved: 2026/02/27 15:07:43 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c))
    visited = [[False] * c for _ in range(r)]
    visited[start_r][start_c] = True

    main_list = []

    while queue:    
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < r and 0 <= nc < c:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                
                    if cheese[nr][nc] == 1:
                        main_list.append((nr, nc))

                    else:
                        queue.append((nr, nc))
    
    for i, j in main_list:
        cheese[i][j] = 0
    
    return len(main_list)


r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]

time = 0
final_cnt = 0

while True:
    cnt = bfs(0, 0)

    if cnt == 0:
        break

    final_cnt = cnt
    time += 1

print(time)
print(final_cnt)
