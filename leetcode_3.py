#LeetCode 3 - Longest Substring Without Repeating Characters


def length_of_longest_substring(s):
    result = 0

    chars = {}
    l, r = 0, 0

    while r < len(s):
        if s[r] not in chars or (s[r] in chars and chars[s[r]] < l):
            result = max(result, r - l + 1)
        else:
            l = chars[s[r]] + 1
        chars[s[r]] = r

        r += 1
    return result
