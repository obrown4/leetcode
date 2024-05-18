#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Evaluate Reverse Polish Notation #150

import math
def evalRPN(tokens: list[str]) -> int:
    ops = {'+', '-', '*', '/'}
    stack = []

    for t in tokens:
        if t not in ops:
            stack.append(int(t))
        else:
            b, a = stack.pop(), stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(math.trunc(a * b))
            elif t == '/':
                stack.append(math.trunc(a / b))

    return stack[-1]
