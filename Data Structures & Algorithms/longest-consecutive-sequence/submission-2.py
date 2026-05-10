class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        con = set(nums)
        longest = 0
        for i in con:
            # find the start of sequence
            if i - 1 not in con:
                length = 0
                while i + length in con:
                    length += 1
                longest = max(longest, length)
        return longest