#Leetcode 74 - Search a 2D Matrix


def search_matrix(matrix, target):

    def binary_search(nums):

        start, end = 0, len(nums) - 1
        
        while end >= start:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return False


    start, end = 0, len(matrix) - 1

    while end >= start:
        mid = (end + start) // 2

        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            last_item_of_row = matrix[mid][len(matrix[mid]) - 1]
            
            if last_item_of_row == target:
                return True
            elif last_item_of_row > target:
                return binary_search(matrix[mid])
            else:
                start = mid + 1
        else:
            end = mid - 1
