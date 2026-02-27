from collections import deque
import copy

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

max_safe_area = 0

def make_walls(count, start_idx):
    global max_safe_area

    if count == 3:
        new_board = copy.deepcopy(board)

        queue = deque(viruses)

        # 바이러스 확산
        while queue:
            cur_r, cur_c = queue.popleft()

            for d in range(4):
                nr = cur_r + dr[d]
                nc = cur_c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    if new_board[nr][nc] == 0:
                        new_board[nr][nc] = 2
                        queue.append((nr, nc))
        
        # 확산 후 안전한 공간 세기
        safe_area = 0
        for row in range(N):
            for col in range(M):
                if new_board[row][col] == 0:
                    safe_area += 1

        # 안전 영역 최대 크기 
        if safe_area > max_safe_area:
            max_safe_area = safe_area
        
        return
    
    # 벽 세우기 (꼭 바이러스 근처에 세울 필요 없음)
    for i in range(start_idx, len(empty_spaces)):
        r, c = empty_spaces[i]

        board[r][c] = 1

        make_walls(count+1, i+1)

        board[r][c] = 0



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

empty_spaces = []
viruses = []

for row in range(N):
    for col in range(M):
        if board[row][col] == 2:
            viruses.append((row, col))
        if board[row][col] == 0:
            empty_spaces.append((row, col))

make_walls(0, 0)
print(max_safe_area)