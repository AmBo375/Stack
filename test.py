from StackArray import *


def balanced(alg):
    stack = StackArr()
    expr = {"{": "}", "[": "]", "(": ")"}
    for i in alg:
        if i in ("{", "[", "("):
            stack.push(i)
        elif expr.get(stack.peek()) == i:
            print(i)
            print("popped")
            stack.pop()
    if stack.size() != 0:
        print(alg, ": not balanced")
    else:
        print(alg, ": balanced")


if __name__ == '__main__':
    formula_expr = "())"
    balanced(formula_expr)
