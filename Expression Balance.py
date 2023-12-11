from StackSLL import *


def balanced(alg):
    stack = StackSLL()
    len_expr = 0
    expr = {"{": "}", "[": "]", "(": ")"}
    for i in alg:
        if i in ("{", "[", "("):
            stack.push(i)
        elif expr.get(stack.peek()) == i:
            stack.pop()
        len_expr += 1
    if stack.size != 0 or len_expr % 2 != 0:
        print(alg, ": not balanced")
    else:
        print(alg, ": balanced")


if __name__ == '__main__':
    formula_expr = "())"
    balanced(formula_expr)
