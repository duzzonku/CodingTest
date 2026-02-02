n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

count_dict = {}

for card in arr1:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1

answer = []

for target in arr2:
    if target in count_dict:
        answer.append(count_dict[target])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))