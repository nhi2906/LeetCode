class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]