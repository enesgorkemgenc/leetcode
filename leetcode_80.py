#LeetCode 80 - Remove Duplicates from Sorted Array II


def remove_duplicates(nums):

    l = 0
    counter = 1

    for i in range(1, len(nums)):

        if nums[i] == nums[l]:
            counter += 1
            if counter < 3:
                l += 1
        
        else:
            
            


    return nums

print(remove_duplicates([0,0,1,1,1,1,2,3,3]))
