#LeetCode 125 - Valid Palindrome


def is_palindrome(s):
    
    p1, p2 = 0, len(s) -1

    while p1 < p2:

        while not s[p1].isalnum():
            p1 += 1
            if p1 > len(s) -1:
                return True

        while not s[p2].isalnum():
            p2 -= 1
            if p2 < 0:
                return True

        if s[p1].lower() != s[p2].lower():
            return False
        
        p1 += 1
        p2 -= 1
        
    return True


def is_palindrome_2(s):

    l, r = 0, len(s) - 1 

    while l < r:

        while not s[l].isalnum():
            l += 1
            if l > len(s) -1:
                return True
            
        while not s[r].isalnum():
            r -= 1
            if r < 0:
                return True
            
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1

    return True
