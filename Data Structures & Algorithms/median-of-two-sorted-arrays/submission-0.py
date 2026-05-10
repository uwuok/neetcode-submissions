class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        print(nums)
        if len(nums) & 1:
            return nums[len(nums) // 2]
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
