class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key = num, value = cnt
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # index = cnt, value = num
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            if len(freq[i]): # 可省略
                for n in freq[i]:
                    ans.append(n)
                if k == len(ans):
                    return ans
        return ans