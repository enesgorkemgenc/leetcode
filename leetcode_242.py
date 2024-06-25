#LeetCode 242 - Valid Anagram


#Attempt 1
def valid_anagram(s, t):

    if len(s) != len(t):
        return False

    chars_map = {}

    for i in range(len(s)):
        char_of_s = s[i]
        char_of_t = t[i]

        if chars_map.get(char_of_s):
            chars_map[char_of_s] += 1
        else:
            chars_map[char_of_s] = 1

        if chars_map.get(char_of_t):
            chars_map[char_of_t] -= 1
        else:
            chars_map[char_of_t] = -1

    
    for char in chars_map:
        if chars_map[char]:
            return False
        
    return True


#TODO: I will get back to here later.
