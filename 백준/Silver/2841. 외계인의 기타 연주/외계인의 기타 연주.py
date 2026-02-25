import sys

input = sys.stdin.readline

N, P = map(int, input().split())


stacks = [[] for _ in range(7)] 
cnt = 0

for _ in range(N):
    line, fret = map(int, input().split()) 

    while stacks[line] and stacks[line][-1] > fret:
        stacks[line].pop()
        cnt += 1

    if stacks[line] == fret:
        continue

    if not stacks[line] or stacks[line][-1] < fret:
        stacks[line].append(fret)
        cnt += 1
    
print(cnt)