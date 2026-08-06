class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if c == ')' or c == '}' or c == ']':
                if len(stack) == 0:
                    return False
                check = stack.pop()
                if c == ')' and check != '(':
                    return False
                if c == '}' and check != '{':
                    return False
                if c == ']' and check != '[':
                    return False
        if len(stack) != 0:
            return False
        return True