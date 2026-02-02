import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    com = input().strip().split()

    if com[0] == 'push':
        stack.append(com[1])

    elif com[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(-1))

    elif com[0] == 'size':
        print(len(stack))

    elif com[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif com[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])