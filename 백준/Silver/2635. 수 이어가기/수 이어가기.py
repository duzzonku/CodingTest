n = int(input())

max_list = []

for second in range(1, n + 1):
    temp_list = [n, second]

    while True:
        next_num = temp_list[-2] - temp_list[-1]

        if next_num < 0:
            break

        temp_list.append(next_num)

    if len(max_list) < len(temp_list):
        max_list = temp_list

print(len(max_list))
print(*max_list)