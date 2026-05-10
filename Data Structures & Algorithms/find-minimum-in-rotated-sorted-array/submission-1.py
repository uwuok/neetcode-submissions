class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]
        
        while l <= r:
            # 如果整個區間是遞增的，nums[l] 就是最小值
            if nums[l] <= nums[r]:
                ans = min(ans, nums[l])
                break

            m = (l + r) // 2
            ans = min(ans, nums[m])

            if nums[m] >= nums[l]:  
                # 左半部是遞增的，所以最小值一定在右半邊
                l = m + 1
            else:  
                # 右半部是遞增的，所以最小值在左半邊
                r = m - 1
        
        return ans
