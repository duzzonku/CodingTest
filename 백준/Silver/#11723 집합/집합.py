#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11723                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11723                          #+#        #+#      #+#     #
#    Solved: 2026/01/29 16:55:08 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

M = int(input())
s = set()

for idx in range(M):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set(i for i in range(1,21))
        elif tmp[0] == 'empty':
            s.clear()
    else:
        command, target = tmp[0], tmp[1]
        target = int(target)

        if command == 'add':
            s.add(target)

        elif command == 'remove':
            s.discard(target)
    
        elif command == 'check':
            print(1 if target in s else 0 )
    
        elif command == 'toggle':
            if target in s:
                s.discard(target)
            else:
                s.add(target)
