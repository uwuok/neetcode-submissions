class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        left_total = (n + m + 1) // 2
        lo, hi = 0, n
        while lo <= hi:
            # i: nums1 split pos
            # j: nums2 split pos
            i = (lo + hi) // 2
            j = left_total - i
            l1 = nums1[i - 1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < n else float('inf')
            l2 = nums2[j - 1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < m else float('inf')
            if l1 <= r2 and l2 <= r1:
                if (n + m) & 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                hi = i - 1
            else:
                lo = i + 1
        return -1