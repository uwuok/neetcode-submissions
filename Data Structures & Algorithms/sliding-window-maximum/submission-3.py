class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 單調遞減 queue, 保存元素的 index 
        window = deque()
        result = []

        for i in range(len(nums)):
            # 刪除過期元素 不在 [i-k+1, i]
            if window and window[0] < i - k + 1:
                window.popleft()
            
            # 剔除不可能成為最大值的元素
            # 如果新加入的 nums[i] > deque 尾端，則尾端元素永遠不可能是最大值了
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            
            # 將當前元素的索引加入進去
            window.append(i)

            # 當 window 大小達到 k，開始記錄答案
            if i >= k - 1:
                result.append(nums[window[0]])
        return result