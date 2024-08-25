#LeetCode 26 - Remove Duplicates from Sorted Array


def remove_duplicates_1(nums):

    l = 0

    for r in range(len(nums)):
        
        if nums[r] != nums[l]:
            nums[r], nums[l+1] = nums[l], nums[r]
            l += 1

    return l+1


def remove_duplicates(nums):
    
    k = 0

    for i, num in enumerate(nums):
        
        if num > nums[k]:
            nums[k + 1], nums[i] = nums[i], nums[k + 1]
            k += 1

    return k + 1
