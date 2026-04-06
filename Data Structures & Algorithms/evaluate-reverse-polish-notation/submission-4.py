class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for r in range(len(tokens)):
            if tokens[r] not in ("+", "-", "*", "/"):
                stack.append(int(tokens[r]))
            else:
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.pop()
                if tokens[r] == "+":
                    stack.append(b+a)
                elif tokens[r] == "-":
                    stack.append(b-a)
                elif tokens[r] == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
        return stack[-1]