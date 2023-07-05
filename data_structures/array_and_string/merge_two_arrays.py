# 1 2 5 10 12
#     ^
# 3 4 8 15 20
#   ^
# 1 2 3 4
# two pointer method
# O(n + m) - space
# O (n + m) - time
def merge_two_sorted_arrays(arr1: list[int], arr2: list[int]) -> list:
    i = j = 0
    result = []
    n, m = len(arr1), len(arr2)
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < n:
        result.append(arr1[i])
        i += 1
    while j < m:
        result.append(arr2[j])
        j += 1
    return result
# I can use yield instead of result because this function uses no space at all


