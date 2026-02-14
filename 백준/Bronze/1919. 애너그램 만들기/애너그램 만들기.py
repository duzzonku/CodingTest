word1 = input()
word2 = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

cnt = 0

for char in alphabet:
    num1 = word1.count(char)
    num2 = word2.count(char)

    cnt += abs(num1-num2)

print(cnt)