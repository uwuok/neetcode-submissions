class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if table.get(nums[i], None) != None:
                # print(table.get(nums[i]), i)
                return list([table[nums[i]], i])
            else:
                table[diff] = i
        # print(123)
        # table = {4:0, , }
        return list()