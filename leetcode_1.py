#LeetCode 1 - Two Sum


#Attempt 1
def two_sum(nums, target):

    numbers_map = {}

    for i in range(len(nums)):
        number = nums[i]
        number_to_find = target - number

        if number_to_find in numbers_map:
            return [numbers_map[number_to_find], i]
        else:
            numbers_map[number] = i
