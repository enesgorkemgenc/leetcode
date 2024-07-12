#LeetCode 26 - Remove Duplicates from Sorted Array


def remove_duplicates(nums):

    l = 0

    for r in range(len(nums)):
        
        if nums[r] != nums[l]:
            nums[r], nums[l+1] = nums[l], nums[r]
            l += 1

    return l+1
