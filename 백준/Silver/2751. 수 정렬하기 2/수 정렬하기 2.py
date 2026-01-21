import sys
N = int(sys.stdin.readline())

my_number=[]

for i in range(1,N+1):
    number = int(sys.stdin.readline())
    my_number.append(number)
    
my_number = list(set(my_number))
my_number.sort()

for n in my_number:
    print(n)