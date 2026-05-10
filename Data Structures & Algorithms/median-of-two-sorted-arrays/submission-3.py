class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        # 左半部份需要有的數量
        half = (n + m + 1) // 2
        l, r = 0, n
        while l <= r:
            # i = nums1 的劃分點
            # j = nums2 的劃分點
            i = (l + r) // 2
            j = half - i
            l1 = nums1[i - 1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < n else float('inf')
            l2 = nums2[j - 1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < m else float('inf')
            # 如果劃分點合理
            if l1 <= r2 and l2 <= r1:
                if (n + m) & 1:
                    # 劃分點左半部份最大值
                    return max(l1, l2)
                else:
                    # 劃分點左半部分最大值 + 右半部分最小值後除以2
                    return (max(l1, l2) + min(r1, r2)) / 2
            # 如果劃分點不合理，進行更新
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1
        return -1