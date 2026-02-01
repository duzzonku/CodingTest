import sys
input = sys.stdin.readline

n = int(input())
count_list = [0] * 10001

for i in range(n):
    num = int(input())
    count_list[num] += 1

for j in range(10001):
    if count_list[num] != 0:
        for k in range(count_list[j]):
            print(j)