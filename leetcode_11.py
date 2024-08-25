#LeetCode 11 - Container With Most Water


def max_area_1(height):

    max_area_result = 0

    l, r = 0, len(height) - 1

    while l < r:
        max_height = height[r] if height[l] > height[r] else height[l]
        area = max_height * (r - l)

        max_area_result = area if area > max_area_result else max_area_result

        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return max_area_result



def max_area(heights):

    current_max_area = 0
    l, r = 0, len(heights) - 1

    while l < r:
        width = r - l
        height = min(heights[l], heights[r])

        current_max_area = max(current_max_area, width * height)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return current_max_area
