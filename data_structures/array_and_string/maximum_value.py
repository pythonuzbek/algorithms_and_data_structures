def max_integer(array: list) -> int:
    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
    return array[-1]


l = [20, 30, 60, 50, 40]
print(max_integer(l))
