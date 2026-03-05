hex_dict = {
    '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]

    password = []

    for r in range(N):
        for c in range(M - 1, -1, -1):
            if board[r][c] == '1':
                target = board[r][c - 55: c + 1]

                for i in range(0, 56, 7):
                    number = target[i: i + 7]
                    password.append(hex_dict[number])
                break

        if len(password) == 8:
            break

    odd_sum = 0
    for i in range(0, 8, 2):
        odd_sum += password[i]

    even_sum = 0
    for j in range(1, 8, 2):
        even_sum += password[j]

    result = odd_sum * 3 + even_sum
    if result % 10 == 0:
        print(f'#{tc} {odd_sum + even_sum}')
    else:
        print(f'#{tc} 0')
