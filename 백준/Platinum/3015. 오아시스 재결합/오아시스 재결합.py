import sys
input = sys.stdin.readline

N = int(input())
height = [int(input()) for _ in range(N)]

stack = []
pairs = 0

for i in height:
    cnt = 1

    while stack and stack[-1][0] <= i:
        top_height, top_cnt = stack.pop()

        pairs += top_cnt

        if top_height == i:
            cnt += top_cnt

    if stack:
        pairs += 1

    stack.append((i, cnt))

print(pairs)