class Solution {
    public int singleNumber(int[] nums) {
        // 由於每個值會出現兩次，所以只要找到哪個 bit manipulation 可以做到相同值為 0
        // 的操作，而 XOR 可以做到這樣
        // 然後由於 XOR 具有交換性的操作，所以 [3, 2, 3] 可以轉換成 [3, 3, 2]
        // 3 ^ 3 = 0, 0 ^ 2 = 2
        
        int res = nums[0];
        for (int i = 1; i < nums.length; ++i) {
            res ^= nums[i];
        }
        return res; 
    }
}
