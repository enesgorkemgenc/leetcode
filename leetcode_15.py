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
