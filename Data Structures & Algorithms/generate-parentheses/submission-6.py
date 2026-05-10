class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(left: int = 0, right: int = 0):
            if left == right == n:
                res.append("".join(stack))
                return
            if left < n:
                stack.append('(')
                backtrack(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(')')
                backtrack(left, right + 1)
                stack.pop()
        backtrack()
        return res