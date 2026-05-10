class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        prefix[0] = nums[0]
        postfix[len(nums) - 1] = nums[len(nums) - 1]
        # postfix = [, , , ,]
        # nums = [1, 2, 4, 6]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i - 1]
            postfix[len(nums) - i - 1] = nums[len(nums) - i - 1] * postfix[len(nums) - i]
        print(nums)
        print(prefix)
        print(postfix)
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(1 * postfix[i + 1])
            elif i == len(nums) - 1:
                res.append(prefix[i - 1] * 1)
            else:
                res.append(prefix[i - 1] * postfix[i + 1])
        return res
