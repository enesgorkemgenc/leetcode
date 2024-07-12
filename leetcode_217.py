#LeetCode 217 - Contains Duplicate


def contains_duplicate(nums):

    numbers_set = set()

    for number in nums:
        if number in numbers_set:
            return True
        else:
            numbers_set.add(number)

    return False


#I believe using else even if there is a return statement, has better readability.
