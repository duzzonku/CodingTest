def dfs(start, l):
    if len(result) == l:

        vowel_count = 0
        consonant_count = 0

        for char in result:
            if char in 'aeiou':
                vowel_count += 1
            else:
                consonant_count += 1
        
        if vowel_count >= 1 and consonant_count >= 2:
            print(''.join(result))
            return
    
    for i in range(start, C):
        result.append(data[i])
        dfs(i+1, l)
        result.pop()

    return


L, C = map(int, input().split())
data = list(input().split())

data.sort()
result = []

dfs(0, L)