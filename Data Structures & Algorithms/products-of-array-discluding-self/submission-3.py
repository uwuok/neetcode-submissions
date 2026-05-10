class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 將 res 的 elements 全設為 1
        res = [1] * len(nums)
        # 將 prefix 的結果存放至 res 中
        # 可以注意的是：我們是從第二個元素開始，因為第一個元素已經是 1
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        # 接下來要進行 postfix 的計算，postfix 的計算是逆序的
        # 這邊一樣略過一個 element，因為 postfix 
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # 簡單理解就是：prefix * postfix
            res[i] *= postfix
            postfix *= nums[i]
        return res

