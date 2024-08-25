#LeetCode 75 - Sort Colors


#This solution doesn't use two pointers.
def sort_colors_1(nums):

    color_counts = {
        0: 0,
        1: 0,
        2: 0,
    }

    for num in nums:
        color_counts[num] += 1
    

    for i in range(len(nums)):

        if i < color_counts[0]:
            nums[i] = 0

        elif i < color_counts[0] + color_counts[1]:
            nums[i] = 1
            
        elif i < color_counts[0] + color_counts[1] + color_counts[2]:
            nums[i] = 2
    
    return nums


#Failed
def sort_colors_attempt_2(nums):

    c_l, l, r = 0, 0, len(nums) - 1

    while l < r:

        while nums[c_l] == 0:
            c_l += 1
            l += 1

            if c_l == len(nums):
                return nums

        while nums[r] == 2:
            r -= 1
            if r == 0:
                return nums


        if nums[l] > nums[r]:

            nums[r], nums[c_l] = nums[c_l], nums[r]

            if nums[l] == 0:
                c_l += 1
                l += 1
            if nums[r] == 2:
                r -= 1
        else:
            l += 1

    return nums


#Successful
def sort_colors(nums):

    r, b = 0, len(nums) - 1
    i = 0

    while i < b + 1:
        num = nums[i]

        if num == 0:
            nums[r], nums[i] = nums[i], nums[r]
            r += 1
        elif num == 2:
            nums[b], nums[i] = nums[i], nums[b]
            b -= 1
            i -= 1
        i += 1

    return nums
