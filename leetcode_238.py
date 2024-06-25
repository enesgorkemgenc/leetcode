#LeetCode 217 - Product of Array Except Self


#Note: I watched the solution of this a few days ago. 

#Attempt 1
def product_except_self(nums):

    products_from_left = [1] * len(nums)
    products_from_right = [1] * len(nums)

    for i in range(len(nums)):

        products_from_left[i] = nums[i] * products_from_left[i-1]
        products_from_right[i] = nums[-i-1] * products_from_right[i-1]

    products_from_right.reverse()

    result = [None] * len(nums)

    for i in range(len(nums)):

        product_left = products_from_left[i-1] if i != 0 else 1
        product_right = products_from_right[i+1] if i < len(nums)-1 else 1

        result[i] = product_left * product_right

    return result


#TODO: I will get back to here later.
