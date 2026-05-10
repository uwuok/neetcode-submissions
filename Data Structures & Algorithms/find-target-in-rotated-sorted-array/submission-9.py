# 解題方式：
# 由於題目特性，必定存在純粹升序的範圍
# 可透過繪製圖來標示出升序以及有可能重製的範圍
# 再依據範圍進行條件判斷撰寫

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # 如果 [l, m] 是升序排序好的 (LEFT segment is sorted)
            if nums[l] <= nums[m]:
                # 如果 target 不在 LEFT segment 內
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # 如果 [m, r] 是升序排序好的 (RIGHT segment is sorted)
            else:
                # 如果 target 不在 RIGHT segment 內
                if target < nums[m] or target > nums[r]:
                    r = m - 1 
                else:
                    l = m + 1
        return -1