class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        left, right  = 0, 0
        window = deque([])
        cur_max = -10001
        # while right < k:
        #     # if nums[right] > cur_max:
        #     #     cur_max = nums[right]
        #     window.append(nums[right])
        #     right += 1
        # print(window)

        while right < k:
            window.append(nums[right])
            right += 1

        result = []
        while right < len(nums):
            
            result.append(max(window))
            window.append(nums[right])
            window.popleft()
            
            
            right += 1
        result.append(max(window))

        return result
        # 等於要一直維護 window 內最大的數值是多少
        # 可能會因為移出或是加入影響該數值

        # while right < len(nums):
        #     cur_max = -10000 - 1

        #     if drop_num == cur_max:
        #         # 要重新尋找最大值
        #         # 我能否建表處理呢？

        #     if new_num > cur_max:
        #         cur_max = new_num 