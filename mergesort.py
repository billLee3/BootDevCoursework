def merge_sort(nums):
    if (len(nums) == 0):
        return nums
    if (len(nums) < 2):
        return nums
 
    middle_index = len(nums)//2
    first_list = nums[:middle_index]
    second_list = nums[middle_index:]
    sorted_left = (merge_sort(first_list))
    sorted_right = (merge_sort(second_list))
    return merge(sorted_left, sorted_right)
    


def merge(first, second):
    final = []
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] > second[j]:
            final.append(second[j])
            j +=1
        else:
            final.append(first[i])
            i +=1
        
    final.extend(first[i:])
    final.extend(second[j:])
    return final
