class Solution:

    def encode(self, strs: List[str]) -> str:
        # 只有數字的話，會不知道究竟數字有多長
        # res = ''.join(str(len(s)) + '#' + s for s in strs)
        return ''.join((f'{len(s)}#{s}') for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        return res