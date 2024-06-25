#LeetCode 49 - Group Anagrams


#Attempt 1
def group_anagrams(strs):

    grouped_anagrams = {}

    for str in strs:
        chars_map = {}

        for i in range(len(str)):
            char = str[i]

            if chars_map.get(char):
                chars_map[char] += 1
            else:
                chars_map[char] = 1

        hashed_chars_map = frozenset(chars_map.items())

        if grouped_anagrams.get(hashed_chars_map):
            grouped_anagrams[hashed_chars_map].append(str)
        else:
            grouped_anagrams[hashed_chars_map] = [str]
        
    return list(grouped_anagrams.values())
