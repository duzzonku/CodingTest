#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1874                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1874                           #+#        #+#      #+#     #
#    Solved: 2026/02/25 15:39:52 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

stack = []
current = 1
op = []
possible = True


for tc in range(n):
    num = int(input())

    while current <= num:
        stack.append(current)
        op.append('+')
        current += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')

    else:
        possible=False
        break

if possible:
    for i in op:
        print(i)
else:
    print('NO')