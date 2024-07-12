#LeetCode 36 - Trapping Rain Water


#Stopped because I found a better idea
def trap_attempt_1(height):

    s, e = 0, 1 #trap start - end

    current_trap_start_height = 0

    while s < len(height) - 1:

        #find trap start for s

        if height[s] > current_trap_start_height:
            current_trap_start_height = height[s]

            e = s + 1

            while height[e] > height[e - 1]:
                e += 1