#LeetCode 15 - 3Sum


def three_sum_attempt_1(nums):
    
    numbers_map = {}
    triplets_map = {}

    for i in range(len(nums)):
        numbers_map[nums[i]] = i

    for p1 in range(len(nums)-1):
        for p2 in range(p1+1, len(nums)):

            number_1 = nums[p1] 
            number_2 = nums[p2]

            number_to_look_for = -1 * (number_1 + number_2)

            if number_to_look_for in numbers_map and numbers_map[number_to_look_for] != p1 and numbers_map[number_to_look_for] != p2:
                
                triplets_map[''.join(str(x) for x in sorted([number_1, number_2, number_to_look_for]))] = [number_1, number_2, number_to_look_for]
            
    return triplets_map.values()


def three_sum_attempt_2(nums):

    result = []

    nums_set = {}

    nums.sort()

    for i, num in enumerate(nums):
        if num in nums_set:
            nums_set[num].append(i)
        else:
            nums_set[num] = [i]

    l, r = 0, len(nums) - 1

    for l in range(len(nums)):

        for r in reversed(range(l + 1, len(nums))):
            r = len(nums) + 1 - r
            num_to_look_for = -1 * (nums[l] + nums[r])
        
            if num_to_look_for <= nums[r] and num_to_look_for >= nums[l]:
                if num_to_look_for in nums_set:
                    for i in nums_set[num_to_look_for]:
                        if i < r and i > l:
                            if not [nums[l], num_to_look_for, nums[r]] in result: 
                                result.append([nums[l], num_to_look_for, nums[r]])
                                break
    return result


def three_sum(nums):

    result = []

    nums.sort()

    for i, num in enumerate(nums):
        l, r = i + 1, len(nums) - 1

        if i > 0 and num == nums[i - 1]:
            continue

        while l < r:
            total = num + nums[l] + nums[r]

            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([num, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return result
