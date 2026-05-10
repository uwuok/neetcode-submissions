class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        # sign_stack = []
        for s in tokens:
            if s[0] == '-' and len(s) > 1 or s.isdigit():
                num_stack.append(int(s))
            else:
                print(num_stack)
                b = num_stack.pop()
                a = num_stack.pop()
                if s == '+':
                    num_stack.append(a + b)
                elif s == '-':
                    num_stack.append(a - b)
                elif s == '*':
                    num_stack.append(a * b)
                elif s == '/':
                    num_stack.append(int(a / b))
        return num_stack[0]

