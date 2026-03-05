N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

min_diff = 9999999

def dfs(depth, idx):
    global min_diff

    if depth == N//2:
        start_power = 0
        link_power = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start_power += S[i][j]
                
                elif not visited[i] and not visited[j]:
                    link_power += S[i][j]

        diff = abs(start_power - link_power)
        min_diff = min(min_diff, diff)
        
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(min_diff)
