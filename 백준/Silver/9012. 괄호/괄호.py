import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    stack = []
    data = input().strip()
    is_vps = True

    for char in data:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_vps = False
                break
            else:
                stack.pop()
    
    if stack or not is_vps:
        print('NO')
    else:
        print('YES')

