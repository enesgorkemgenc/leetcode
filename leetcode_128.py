#LeetCode 128 - Longest Consecutive Sequence


def longest_consecutive_attempt_1(nums):
    
    nums_map = set()
    
    longest_consecutive_result = 0

    for num in nums:
        nums_map.add(num)

    for num in nums:
        count_of_numbers_consecutive = 1
        starting_number = num

        while (starting_number + count_of_numbers_consecutive) in nums_map:
            count_of_numbers_consecutive += 1
        
        longest_consecutive_result = max(longest_consecutive_result, count_of_numbers_consecutive)

    return longest_consecutive_result


def longest_consecutive_attempt_2(nums):
    
    nums_map = set()
    
    longest_consecutive_result = 0

    for num in nums:
        nums_map.add(num)

        count_of_numbers_consecutive = 1
        starting_number = num

        while (starting_number + count_of_numbers_consecutive) in nums_map:
            count_of_numbers_consecutive += 1
        
        longest_consecutive_result = max(longest_consecutive_result, count_of_numbers_consecutive)

        count_of_numbers_consecutive = 1

        while (starting_number + -count_of_numbers_consecutive) in nums_map:
            count_of_numbers_consecutive += 1

        longest_consecutive_result = max(longest_consecutive_result, count_of_numbers_consecutive)

    return longest_consecutive_result


def longest_consecutive_attempt_3(nums):

    numbers_map = set()

    longest_consecutive_result = 0

    for number in nums:
        numbers_map.add(number)

        i = 0

        while number - i in numbers_map:
            i+=1
        
        starting_number = number - i + 1

        count_of_numbers_consecutive = 1

        while starting_number + count_of_numbers_consecutive in numbers_map:
            count_of_numbers_consecutive += 1

        longest_consecutive_result = max(count_of_numbers_consecutive, longest_consecutive_result)
        
    return longest_consecutive_result


#Attempt 4: After a ton of thinking, I'm going to try something really different.
def longest_consecutive(nums):
    
    max_consecutive_result = 0

    number_consecutive_lengths = {}
    refferer_numbers = {}

    for number in nums:
        
        refs = refferer_numbers.get(number)

        if refs:
            total_consecutive = 1 if len(refs) == 2 else 0
            for ref in refs:
                if len(refs) == 1:
                    number_consecutive_lengths[ref] += 1
                total_consecutive += number_consecutive_lengths[ref]

                if number > ref:
                    #change key with +1
                    new_key = number + 1
                    if refferer_numbers.get(new_key):
                        refferer_numbers[new_key].append(ref)
                    else:
                        refferer_numbers[new_key] = [ref]

                else:
                    #change key with -1
                    new_key = number - 1
                    if refferer_numbers.get(new_key):
                        refferer_numbers[new_key].append(ref)
                    else:
                        refferer_numbers[new_key] = [ref]

            for ref in refs:
                number_consecutive_lengths[ref] = total_consecutive


            max_consecutive_result = max(max_consecutive_result, total_consecutive)

        else:
            if not number_consecutive_lengths.get(number):
                number_consecutive_lengths[number] = 1
                
                if refferer_numbers.get(number-1):
                    refferer_numbers[number-1].append(number)
                else:
                    refferer_numbers[number-1] = [number]

                if refferer_numbers.get(number+1):
                    refferer_numbers[number+1].append(number)
                else:
                    refferer_numbers[number+1] = [number]
        
    return max_consecutive_result


#I'm giving a break here after an hour.
