class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {'}' : '{', ']' : '[', ')' : '('}
        stack = []
        for c in s:
            if c in close_open:
                if stack and stack[-1] == close_open[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return False if stack else True
