class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median = 第 k 個大的數(k = (len(nums1) + len(nums2)) // 2)
        # 透過維護 nums1，讓其值皆小於 nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left_total = (m + n + 1) // 2

        l, r = 0, m
        while l <= r:
            i = (l + r) // 2 # 表示 nums1 的切割點
            # 表示 nums2 的切割點，減去 nums1 所貢獻的左半邊數量
            # 剩餘為 nums2 可貢獻的左半邊數量
            j = left_total - i 
            l1 = nums1[i - 1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')
            l2 = nums2[j - 1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m + n) & 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                r = i - 1
            else:
                l = i + 1
        return -1