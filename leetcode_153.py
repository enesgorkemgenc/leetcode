#LeetCode 153 - Find Minimum in Rotated Sorted Array


def find_min(nums):
    l, r = 0, len(nums) - 1

    while nums[l] > nums[r]:
        mid = (l + r) // 2

        if nums[mid] < nums[l]:
            r = mid
        else:
            l = mid + 1

    return nums[l]
