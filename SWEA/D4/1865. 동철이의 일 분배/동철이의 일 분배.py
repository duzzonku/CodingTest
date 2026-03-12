def backtracking(depth, cur_per):
    global max_per

    if cur_per <= max_per:
        return

    if depth == N:
        max_per = max(cur_per, max_per)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backtracking(depth + 1, cur_per * (P[depth][i] / 100))
            visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    max_per = 0.0

    backtracking(0, 1.0)
    print(f'#{tc} {max_per * 100:.6f}')