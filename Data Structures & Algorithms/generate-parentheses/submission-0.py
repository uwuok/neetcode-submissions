class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def vaild(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False # 如果 open < 0 就表示至少有一個 close 在 open 的左邊並且沒有匹配上
            return not open

        def dfs(s: str):
            if n * 2 == len(s):
                if vaild(s):
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