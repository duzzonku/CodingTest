#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1799                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1799                           #+#        #+#      #+#     #
#    Solved: 2026/03/19 13:32:46 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def dfs(spaces, idx, cur_cnt):
    global current_max

    if idx == len(spaces):
        current_max = max(current_max, cur_cnt)
        return current_max
    
    r, c = spaces[idx]

    if not visited_diagona1[r + c] and not visited_diagona2[r - c + N - 1]:
        visited_diagona1[r + c] = True
        visited_diagona2[r - c + N - 1] = True

        dfs(spaces, idx + 1, cur_cnt + 1)

        visited_diagona1[r + c] = False
        visited_diagona2[r - c + N - 1] = False

    dfs(spaces, idx + 1, cur_cnt)



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

black = []
white = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            if (r + c) % 2 == 0:
                black.append((r, c))
            else:
                white.append((r, c))

visited_diagona1 = [False] * (2 * N - 1)
visited_diagona2 = [False] * (2 * N - 1)
 
ans_black = 0
ans_white = 0


current_max = 0
dfs(black, 0, 0)
ans_black = current_max

current_max = 0
dfs(white, 0, 0)
ans_white = current_max

print(ans_black + ans_white)


