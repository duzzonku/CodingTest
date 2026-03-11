def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left, equal, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return quick_sort(left) + equal + quick_sort(right)


A = list(map(int, input().split()))

ans = quick_sort(A)
print(ans[500000])