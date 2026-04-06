class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            elif x == ')' and (len(stack) < 1 or stack[len(stack)-1] != '(') :
                return False
            elif x == '}' and (len(stack) < 1 or stack[len(stack)-1] != '{'):
                return False
            elif x == ']' and ( len(stack) < 1 or stack[len(stack)-1] != '['):
                return False
            else:
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False
        