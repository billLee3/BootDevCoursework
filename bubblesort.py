def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        if end == 0:
            swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                tmp_num = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp_num
        end -= 1
    return nums
