#Leetcode 167 - Two Sum II - Input Array Is Sorted


def two_sum_1(numbers, target):

    l,r = 0, len(numbers) - 1

    while l < r: 

        sum = numbers[r] + numbers[l]

        if sum > target:
            r -= 1 
        elif sum < target:
            l += 1 
        else:
            return [l + 1, r + 1]


def two_sum_2(numbers, target):

    l, r = 0, len(numbers) - 1

    while l < r:
        sum_ = numbers[l] + numbers[r]

        if sum_ > target:
            r -= 1
        elif sum_ < target:
            l += 1
        else:
            return [l + 1, r + 1]


def two_sum(numbers, target):

    l, r = 0, len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            return [l + 1, r + 1]
