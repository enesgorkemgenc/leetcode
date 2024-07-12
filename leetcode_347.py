#LeetCode 242 - Top K Frequent Elements


def top_k_frequent(nums, k):

    frequency_map = {}

    for num in nums:
        if frequency_map.get(num):
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    return [items[0] for items in sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)][:k]
