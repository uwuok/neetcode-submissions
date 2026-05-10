class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        res = {}
        for s in strs:
            table = [0] * 26
            for c in s:
                table[ord(c) - ord('a')] += 1
            if tuple(table) not in res:
                res[tuple(table)] = []
            res[tuple(table)].append(s)
        return res.values()
        