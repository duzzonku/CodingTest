#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10799                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10799                          #+#        #+#      #+#     #
#    Solved: 2026/02/25 17:29:16 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
stick = input()

stack = []
cnt = 0

for i in range(len(stick)):
    if stack and stick[i] == ')':
        if stick[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

    if stick[i] == '(':
        stack.append(stick[i])

print(cnt)