N, K = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

top = factorial(N)
bottom = factorial(K)*factorial(N-K)
print(top//bottom)

