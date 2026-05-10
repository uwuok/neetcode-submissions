class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for s in tokens:
            if s.isdigit():
                num_stack.append(int(s))
            elif s[0] == '-' and len(s) > 1:
                num_stack.append(int(s))
            else:
                a = num_stack.pop()
                b = num_stack.pop()
                if s == '+':
                    num_stack.append(b + a)
                elif s == '-':
                    num_stack.append(b - a)
                elif s == '*':
                    num_stack.append(b * a)
                elif s == '/':
                    num_stack.append(int(b / a))
        return num_stack[0]
