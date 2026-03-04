import sys
input = sys.stdin.readline


def dfs(start, k):

    if len(result) == 6:
        print(*result)
        return

    for i in range(start, k):
        result.append(S[i])
        dfs(i+1, k)
        result.pop()

    return


while True:
    data = list(map(int, input().split()))

    if data[0] == 0:
        break

    K = data[0]
    S = data[1:]

    result = []

    dfs(0, K)

    print()