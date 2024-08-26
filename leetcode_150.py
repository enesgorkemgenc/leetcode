#LeetCode 150 - Evaluate Reverse Polish Notation


def evalRPN(tokens):

    operated_stack = []

    for token in tokens:

        if token == '+':
            result = operated_stack.pop() + operated_stack.pop()
        elif token == '-':
            n1 = operated_stack.pop()
            n2 = operated_stack.pop()
            result = n2 - n1
        elif token == '*':
            result = operated_stack.pop() * operated_stack.pop()
        elif token == '/':
            n1 = operated_stack.pop()
            n2 = operated_stack.pop()
            result = int(n2 / n1)
        else:
            operated_stack.append(int(token))
            continue

        operated_stack.append(result)

    return operated_stack[0]
