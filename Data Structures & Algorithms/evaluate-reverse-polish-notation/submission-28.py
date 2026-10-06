class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = {"*", "-", "+", "/"}
        for val in tokens:
            if val not in operand:
                stack.append(int(val))
            else:
                if val == "+":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(r + l)
                elif val == "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                elif val == "*":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(r * l)
                elif val == "/":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(int(l / r))
        return stack[0]