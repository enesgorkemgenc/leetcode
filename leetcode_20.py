#LeetCode 20 - Valid Parentheses


def is_valid(s):

    if len(s) < 2:
        return False

    chars = {
        'opening':{
            '(' : ')',
            '[' : ']',
            '{' : '}'
        },
        'closing':{
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
    }

    char_stack = []

    for char in s:
        if char in chars['opening']:
            char_stack.append(char)
        else: 
            if len(char_stack) > 0:
                if char_stack[-1] == chars['closing'][char]:
                    char_stack.pop()
                else:
                    return False
            else:
                return False

    return not char_stack
