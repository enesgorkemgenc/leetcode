#LeetCode 121 - Best Time to Buy and Sell Stock


def max_profit(prices):
    max_profit_possible = 0
    l, r = 0, 1

    while r < len(prices):
        max_profit_possible = max(max_profit_possible, prices[r] - prices[l])

        if prices[r] < prices[l]:
            l  = r
        r += 1
    return max_profit_possible
