def min_value(array: list) -> int:
    main_index = 0
    for i in range(main_index + 1, len(array) - 1):
        if array[main_index] > array[i]:
            main_index = i
    return array[main_index]


l = [20, 70, 50, 30, 55, 60]
print(min_value(l))

def min_integer(array: list) -> int:
    for i in range(0, len(array) - 1):
        if array[i] < array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp
    return array[-1]
