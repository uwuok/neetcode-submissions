class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        # 我想先找到左右兩側是數字或是字母的位置
        # 再判斷該元素值是否相同
        while i < j:
            while i < j and not self.alphaNum(s[i]):
                i += 1
            while i < j and not self.alphaNum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            