class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 次數作為 key, 數字作為 value (list)
        count = {}

        # freq 的 key = 出現次數, value = 數字(list)
        freq = [[] for i in range(len(nums) + 1)]

        # count 的 key = 數字, value = 出現次數
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        
        # 從尾到頭 (尾部比較多)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # 根據 len(res) 即可得知當前選擇了多少個數值
                if len(res) == k:   
                    return res
            