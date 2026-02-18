board = [list(map(int, input().split())) for _ in range(5)]

mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

def check_bingo():
    bingo_cnt = 0

    for row in board:
        if sum(row) == 0:
            bingo_cnt += 1
    
    for i in range(5):
        cnt = 0
        for j in range(5):
            if board[j][i] == 0:
                cnt += 1
        if cnt == 5:
            bingo_cnt += 1

    diag1 = 0
    for i in range(5):
        if board[i][i] == 0:
            diag1 += 1
    if diag1 == 5:
        bingo_cnt += 1

    diag2 = 0
    for i in range(5):
        if board[i][4-i] == 0:
            diag2 += 1
    if diag2 == 5:
        bingo_cnt += 1

    return bingo_cnt

for i in range(25):
    num = mc[i]

    for r in range(5):
        for c in range(5):
            if board[r][c] == num:
                board[r][c] = 0

    if check_bingo() >= 3:
        print(i+1)
        break