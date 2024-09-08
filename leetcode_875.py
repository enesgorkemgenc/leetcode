#Leetcode 875 - Koko Eating Bananas

import math


def min_eating_speed(piles, h):

    l, r = 1, max(piles)
    result = r

    while l <= r:
        mid = (l + r) // 2
        hours = 0

        for p in piles:
            hours += math.ceil(p / mid)

        if hours <= h:
            result = min(result, mid)
            r = mid - 1
        else:
            l = mid + 1

    return result
