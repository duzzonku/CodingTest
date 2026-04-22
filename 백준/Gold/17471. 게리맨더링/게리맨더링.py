from collections import deque


# 1) 구역 나누기 + 최솟값 계산
def part(idx):
    global min_diff

    if idx == N:
        group_a = []
        group_b = []

        # 모든 구역의 배정이 끝났을 때
        for i in range(N):
            if team[i] == 0:
                group_a.append(i)
            else:
                group_b.append(i)

        # 선거구는 최소 하나의 구역을 포함
        if not group_a or not group_b:
            return

        # 두 선거구가 연결되어 있는지 확인
        if is_connected(group_a) and is_connected(group_b):
            sum_a = sum(people[i] for i in group_a)
            sum_b = sum(people[i] for i in group_b)
            diff = abs(sum_a - sum_b)

            if diff < min_diff:
                min_diff = diff

        return

    team[idx] = 0
    part(idx + 1)

    team[idx] = 1
    part(idx + 1)


# 2) 연결되었는지 확인
def is_connected(group):
    if not group:
        return False

    queue = deque()
    queue.append(group[0])

    visited = [False] * (N + 1)
    visited[group[0]] = True
    count = 1

    while queue:
        cur_node = queue.popleft()

        for next_node in adj[cur_node]:
            if next_node in group and not visited[next_node]:
                visited[next_node] = True
                count += 1
                queue.append(next_node)

    return count == len(group)


N = int(input())
people = list(map(int, input().split()))
adj = [[] for _ in range(N)]

for i in range(N):
    info = list(map(int, input().split()))
    cnt = info[0]

    if cnt > 0:
        neighbors = info[1:]
        for neighbor in neighbors:
            adj[i].append(neighbor - 1)

team = [0] * N
min_diff = 99999

part(0)

if min_diff == 99999:
    print(-1)
else:
    print(min_diff)
