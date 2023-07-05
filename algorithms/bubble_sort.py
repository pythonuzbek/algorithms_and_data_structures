def bubble_sort(nums: list[int]) -> list:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble(nums: list[int]) -> list:
    i = 0
    while i < len(nums):
        j = 0
        while j < len(nums) - 1 - i:
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j += 1
        i += 1
    return nums


