class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        right = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                left.append(c)
            else:
                if len(left) < 1:
                    return False
                x = left.pop()
                if x == '[' and c != ']' or x == '(' and c != ')' or x == '{' and c != '}':
                    return False
        if len(left):
            return False            
        return True
        
# [(])
# [( ]