class Solution {
    public int findDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            if (map.get(nums[i]) != null) {
                return nums[i];
            }
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        return -1;
    }
}
