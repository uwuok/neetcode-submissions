class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 假如說有 exact same frequent 的情況？
        res = dict()
        # longest = 0
        for n in nums:
            res[n] = res.get(n, 0) + 1
            # if res[n] > longest:
            #     longest = res[n]
        ans = []
        print(res)
        values = list(res.values())
        while k > 0:
            longest = max(values)
            for key, value in res.items():
                if k <= 0:
                    break
                if value == longest:
                    ans.append(key)
                    values.remove(longest)
                    print(values)
                    print(k)
                    k -= 1
        return ans