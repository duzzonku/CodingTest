def dfs(idx, cnt, total):
    global ans
    
    if idx == N:
        if cnt > 0 and total == S:
            ans += 1
        return

    dfs(idx + 1, cnt + 1, total + arr[idx] )
    dfs(idx + 1, cnt, total)


N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
dfs(0, 0, 0)

print(ans)
