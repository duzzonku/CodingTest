N = int(input())

my_list = []

for i in range(1,N+1):
    word = input()
    my_list.append(word)

my_list = list(set(my_list))
my_list.sort(key=lambda x: (len(x), x))

for w in my_list:
    print(w)


