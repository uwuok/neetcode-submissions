class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            # print(s)
            sc = ''.join(sorted(s))
            # print(sc)
            if sc not in res:
                res[sc] = [s]
            else:
                res[sc].append(s)
        # print(res)
        return list(res.values())