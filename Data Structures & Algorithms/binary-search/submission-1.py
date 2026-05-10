class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        res = -1 

        while left <= right:
            if nums[mid] == target:
                res = mid
                break
            if nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2 
        return res 
        