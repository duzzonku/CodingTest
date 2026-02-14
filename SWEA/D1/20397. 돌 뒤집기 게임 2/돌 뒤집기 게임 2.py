T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        start_idx = i - 1

        for k in range(1, j + 1):
            left = start_idx - k
            right = start_idx + k
            if 0 <= left and right < N:
                if stone[left] == stone[right]:
                    stone[left] = 1 - stone[left]
                    stone[right] = 1 - stone[right]
            else:
                break

    print(f'#{tc}', *stone)