class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0: # 表示當前最小值皆 > 1，因此沒有答案
                break
            if i > 0 and nums[i - 1] == a: # 表示與先前運算的內容相同(重複運算)
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0: # 過小
                    l += 1
                elif threeSum > 0: # 過大
                    r -= 1
                else: # 相等
                    res.append([a, nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    # 避免重複運算
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


