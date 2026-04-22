from collections import deque
import copy

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 터지고 남은 벽돌들을 아래로 밀어내는 함수
def gravity(W, H, board):
    for c in range(W):
        stack = []
        for r in range(H):
            if board[r][c] > 0:
                stack.append(board[r][c])
                board[r][c] = 0

        idx = H - 1
        while stack:
            board[idx][c] = stack.pop()  # LIFO 구조로 아래부터 채움
            idx -= 1


# 벽돌 폭파
def explode_brick(start_r, start_c, W, H, board):
    queue = deque([(start_r, start_c, board[start_r][start_c])])
    board[start_r][start_c] = 0

    while queue:
        cur_r, cur_c, power = queue.popleft()

        for i in range(1, power):  # 벽돌에 적힌 힘
            for d in range(4):
                nr = cur_r + dr[d] * i  # 거리 i를 반드시 곱해줘야 함
                nc = cur_c + dc[d] * i

                if 0 <= nr < H and 0 <= nc < W and board[nr][nc] > 0:
                    # 값이 1인 벽돌은 터지기만 하고 큐에 넣을 필요 없음
                    if board[nr][nc] > 1:
                        queue.append((nr, nc, board[nr][nc]))
                    board[nr][nc] = 0


# 구슬 투하
def dfs(cnt, cur_board, N, W, H):
    global min_brick

    # 현재 남은 벽돌 세기
    current_count = 0
    for row in cur_board:
        for cell in row:
            if cell > 0:
                current_count += 1

    # 1. 종료 조건: 구슬을 다 던졌거나 벽돌이 0개일 때
    if cnt == N or current_count == 0:
        min_brick = min(min_brick, current_count)
        return

    for c in range(W):
        # 해당 열의 가장 윗벽돌 찾기
        r = 0
        while r < H and cur_board[r][c] == 0:
            r += 1

        if r < H:  # 벽돌이 있는 열이라면
            next_board = copy.deepcopy(cur_board)
            explode_brick(r, c, W, H, next_board)
            gravity(W, H, next_board)
            dfs(cnt + 1, next_board, N, W, H)
        else:
            # 해당 열에 벽돌이 없어도 구슬 던진 횟수는 채워야 하므로 최솟값 갱신
            min_brick = min(min_brick, current_count)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    min_brick = 9999
    dfs(0, board, N, W, H)

    print(f'#{tc} {min_brick}')