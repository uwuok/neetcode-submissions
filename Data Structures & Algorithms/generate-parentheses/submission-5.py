from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(s, op, co):
            # op: 已使用的左括號數
            # co: 已使用的右括號數
            if op == co == n:
                res.append(s)
                return
            
            # (若使用 if op <= co, if op > co 這種判斷條件會導致只能匹配出 "()" 或 "()()" 這樣一左一右括號的結果)
            # 可以加左括號 
            if op < n:
                dfs(s + '(', op + 1, co)
            
            # 可以加右括號（右括號數必須小於左括號數）
            if co < op:
                dfs(s + ')', op, co + 1)
        
        dfs('', 0, 0)
        return res
