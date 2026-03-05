import sys
input = sys.stdin.readline

N = int(input())

meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key = lambda x: (x[1], x[0]))

cnt = 0
meeting_end = 0

for start, end in meeting:
    if start >= meeting_end:
        cnt += 1
        meeting_end = end

print(cnt)