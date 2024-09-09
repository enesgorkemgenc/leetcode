#LeetCode 704 - Binary Search


def search(nums, target):

    def binary_search(arr, start, end):

        if end >= start:
            mid = (start + end) // 2
            mid_val = arr[mid]

            if mid_val == target:
                return mid
            elif mid_val > target:
                return binary_search(arr, start, mid - 1)
            else:
                return binary_search(arr, mid + 1, end)

        else:
            return -1
        
    return binary_search(nums, 0, len(nums) - 1)
