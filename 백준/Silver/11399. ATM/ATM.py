n = int(input())
time = list(map(int, input().split()))

time = sorted(time)
total_time = 0
wait_time = 0

for idx in time:
    wait_time += idx 
    total_time += wait_time

print(total_time)