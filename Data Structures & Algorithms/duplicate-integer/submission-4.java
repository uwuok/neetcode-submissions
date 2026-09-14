class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> table = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            Integer n = nums[i];
            if (table.containsKey(n)) {
                return true;
            } else {
                table.put(n, 1);
            }
        }
        return false; 
    }
}