#LeetCode 424 - Longest Repeating Character Replacement


def character_replacement(s, k):

    result = 0
    l =  0

    char_counts = {}
    max_frequent = 0

    for r in range(len(s)):
        char_counts[s[r]] = char_counts.get(s[r], 0) + 1
        max_frequent = max(max_frequent, char_counts[s[r]])

        while (r - l + 1) - max_frequent > k:
            char_counts[s[l]] -= 1
            l += 1

        result = max(result, r - l + 1)

    return result
