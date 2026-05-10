class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def valid(s):
            left, right = 0, 0
            for c in s:
                if c == '(':
                    left += 1
                elif c == ')':
                    right += 1
                if left < right:
                    return False
            return left == right

        def foo(s):
            if len(s) == 2 * n:
                if valid(s):
                    res.append(s)
                return
            foo(s + '(')
            foo(s + ')')
        foo('')
        return res