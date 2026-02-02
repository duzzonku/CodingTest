import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input().strip())

for i in range(n - 7):
    for j in range(m - 7):
        count_w = 0
        count_b = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                current_pixel = (a + b)

                if current_pixel % 2 == 0:
                    if board[a][b] != 'W':
                        count_w += 1
                    if board[a][b] != 'B':
                        count_b += 1

                else:

                    if board[a][b] != 'B':
                        count_w += 1
                    if board[a][b] != 'W':
                        count_b += 1

        result.append(count_w)
        result.append(count_b)

print(min(result))