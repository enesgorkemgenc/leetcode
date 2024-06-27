#Leetcode 167 - Two Sum II - Input Array Is Sorted


#Solved it before..
def two_sum(numbers, target):

    l,r = 0, len(numbers) - 1

    while l < r: 

        sum = numbers[r] + numbers[l]

        if sum > target:
            r -= 1 
        elif sum < target:
            l += 1 
        else:
            return [l + 1, r + 1]