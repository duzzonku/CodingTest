N, K = map(int, input().split())
students = [[0] * 7 for _ in range(2)]

for tc in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

result = 0

for s in range(2):
    for y in range(1, 7):
        cnt = students[s][y]
        if cnt % K != 0:
            result += int(cnt//K)+1
        else:
            result += int(cnt//K)

print(result)