class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return str()
        res = ''.join(str(len(s)) + '#' + s for s in strs)
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        # 4#neet4#code4#love3#you
        # 有可能是空字串 or 空列表
        res = []
        i = 0                # i 作為數字的起始位置
        while i < len(s):
            j = i            # j 作為數字的結束位置的後一位 -> #
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # length 及代表數字的長度
            i = j + 1        # i 作為字串的起始位置
            j = length + i   # j 作為字串的結束位置的後一位 -> 下個數字的位置
            res.append(s[i:j])
            i = j            # 將 i 作為數字的起始位置
        return res
