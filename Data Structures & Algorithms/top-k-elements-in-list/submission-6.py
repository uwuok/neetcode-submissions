class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}      # key = 數字, value = 出現的次數
        for n in nums:
            count[n] = count.get(n, 0) + 1
        print(count)
        # nums 的長度即為數字最大的頻率
        # freq 使用 array 的原因：
        # 1.頻率是在固定的範圍內，
        # 2.若用 hash 會無法確定最大的 key(出現次數)
        freq = [[] for i in range(len(nums) + 1)]
        # 下方為錯誤寫法，空列表 * 任一數都是一個空列表
        # freq = [[] * (len(nums) + 1)]
        for n, c in count.items():
            # index = 出現次數，elements = 數字
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            # 若 freq[i] 為空列表(當前頻率無吻合之數字)，則不會進行循環
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return None
            