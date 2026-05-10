class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = dict()
        b = dict()
        for i in range(len(s)):
            # dict().get(char, default_value)
            a[s[i]] = a.get(s[i], 0) + 1
            b[t[i]] = b.get(t[i], 0) + 1
        
        for c in s:
            if a.get(c) != b.get(c):
                return False
        return True
