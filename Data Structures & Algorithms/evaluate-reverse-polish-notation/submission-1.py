class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                print(op1)
                print(op2)
                stack.append(op1+op2)
                print(stack)
            elif token == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)
                print(stack)

            elif token == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1*op2)
                print(stack)
            elif token == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2/op1))
                print(stack)
            else:
                stack.append(int(token))

        return stack[0]