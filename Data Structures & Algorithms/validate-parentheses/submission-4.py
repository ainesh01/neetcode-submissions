class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c ==")":
                if stack[-1] == "(":
                    stack.pop()
                else: 
                    return False
            elif c =="}":
                if stack[-1] == "{":
                    stack.pop()
                else: 
                    return False
            elif c =="]":
                if stack[-1] == "[":
                    stack.pop()
                else: 
                    return False
        return True