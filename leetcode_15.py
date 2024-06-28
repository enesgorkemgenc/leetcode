#LeetCode 15 - 3Sum


#Attempt 1 FAILED (BECAUSE OF TIME LIMIT)
def three_sum_attempt_1(nums): #28m
    
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


#Attempt 2
def three_sum(nums):
    
    triplets = []

    number_index_map = {}

    nums.sort()
    #[-4, -1, -1, 0, 1, 2]

    for i in range(len(nums)):
        number_index_map[nums[i]] = i

    lp, rp = 0, len(nums) - 1
    
    while lp < rp:
        number_left = nums[lp]
        number_right = nums[rp]

        if rp == lp + 1:
            rp = len(nums) - 1
            lp += 1
            continue

        if number_left == nums[lp - 1]:
            lp += 1
            continue

        if rp < len(nums) - 2 and number_right == nums[rp + 1]:
            rp -= 1
            continue

        number_to_look_for = -1 * (number_left + number_right)

        if number_to_look_for in number_index_map and (number_index_map[number_to_look_for] != lp and number_index_map[number_to_look_for] != rp):
            triplets.append([number_left, number_right, number_to_look_for])

        rp -= 1

    return triplets

print(three_sum([-1,0,1,2,-1,-4]))