def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        # arr = [2, 3, 4, 10, 40]

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
print(binary_search(arr, 0, len(arr) - 1, x))
