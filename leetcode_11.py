#LeetCode 11 - Container With Most Water


def max_area(height):

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

