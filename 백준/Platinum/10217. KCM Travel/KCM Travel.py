import sys

input = sys.stdin.readline

def solve():
    # 1. 입력 처리
    try:
        line = input().split()
        if not line: return
        N, M, K = map(int, line)
    except ValueError: return

    adj = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        adj[u].append((v, c, d))
    
    # [최적화] 비용이 적게 드는 티켓부터 확인하도록 정렬
    for i in range(1, N + 1):
        adj[i].sort(key=lambda x: x[1])

    # dp[cost][city]: 정확히 cost만큼 써서 city에 도착하는 최소 시간
    # 2D 배열을 dp[cost][city] 순서로 구성하는 것이 메모리 접근 효율(Locality)이 좋습니다.
    INF = 10**9
    dp = [[INF] * (N + 1) for _ in range(M + 1)]
    dp[0][1] = 0

    # 2. 비용(c)을 0부터 M까지 순차적으로 탐색
    for c in range(M + 1):
        for u in range(1, N + 1):
            if dp[c][u] == INF:
                continue
            
            cur_time = dp[c][u]
            
            # 현재 도시 u에서 갈 수 있는 다음 도시들 확인
            for v, cost, time in adj[u]:
                next_cost = c + cost
                if next_cost <= M:
                    # 새로운 시간이 기존 기록보다 짧다면 갱신
                    if dp[next_cost][v] > cur_time + time:
                        dp[next_cost][v] = cur_time + time

    # 3. 결과 출력: N번 도시에 도달하는 모든 비용 중 최소 시간 찾기
    min_res = INF
    for c in range(M + 1):
        if dp[c][N] < min_res:
            min_res = dp[c][N]
            
    print(min_res if min_res != INF else "Poor KCM")

# 테스트 케이스 루프
T_str = input().strip()
if T_str:
    T = int(T_str)
    for _ in range(T):
        solve()