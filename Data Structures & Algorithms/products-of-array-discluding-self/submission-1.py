class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # nums = [1, 2, 3, 4]
        for i in range(1, len(nums)):
            # res = [1, 1, 2, 6]
            res[i] = res[i - 1] * nums[i - 1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            # posfitx = [24, 12, 4, 1]
            postfix = postfix * nums[i]
            print(postfix)
        return res