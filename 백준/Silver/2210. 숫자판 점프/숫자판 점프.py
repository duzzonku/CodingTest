from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def dfs(r, c, word):
    if len(word) == 6:
        word_set.add(word)
        return
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, word + board[nr][nc])
    
    return


board = [list(input().split()) for _ in range(5)]
word_set = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(word_set))