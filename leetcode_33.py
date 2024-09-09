#LeetCode 33 - Search in Rotated Sorted Array


def search(nums, target):

    l, r = 0, len(nums) - 1

    while nums[l] > nums[r]:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < nums[l]:
            r = mid
        else:
            l = mid + 1

    #At this point "l" is start index of the original array which comes after the possible rotation.

    if target == nums[-1]:
        return len(nums) - 1
    elif target > nums[-1]:
        l = 0
        r = r - 1
    else:
        #l = l
        r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1
