def insertion_sort(nums):
    nums_copy = nums.copy()
    for i in range(len(nums_copy)):
        j = i
        while j > 0:
            if nums_copy[(j - 1)] > nums_copy[j]:
                nums_copy[j], nums_copy[j-1] = nums_copy[j-1], nums_copy[j]
            j -= 1
    return nums_copy
