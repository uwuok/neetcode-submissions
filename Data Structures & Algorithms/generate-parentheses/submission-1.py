class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open 

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs('') 
        return res
"""
(())
()()

1122
1212
1221
2211
2121


"""