#LeetCode 283 - Move Zeroes


def move_zeroes(nums):

    l = 0

    for r, num in enumerate(nums):

        if num:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums
