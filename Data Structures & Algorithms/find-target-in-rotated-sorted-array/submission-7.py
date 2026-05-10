class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            
            # Check if the LEFT side is sorted
            if nums[l] <= nums[m]:
                # Logic: Check if target is strictly inside the sorted left range
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Otherwise, the RIGHT side is sorted
            else:
                # Logic: Check if target is strictly inside the sorted right range
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1