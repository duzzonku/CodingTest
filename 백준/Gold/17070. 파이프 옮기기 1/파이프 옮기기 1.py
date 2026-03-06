dr = [0, -1, -1]
dc = [1, 1, 0]

cnt = 0
def dfs(r, c, state):
    global cnt

    if r == N-1 and c == N-1:
        cnt += 1
        return 
    
    if state == 0 or state == 2:
        if c + 1 < N and house[r][c + 1] == 0:
            dfs(r, c + 1, 0)

    if state == 1 or state == 2:
        if r + 1 < N and house[r+1][c] == 0:
            dfs(r + 1, c, 1)

    if c + 1 < N and r + 1 < N:
        if house[r+1][c+1] == 0 and house[r+1][c] == 0 and house[r][c+1] == 0:
            dfs(r + 1, c + 1, 2)


N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dfs(0, 1, 0)
print(cnt)