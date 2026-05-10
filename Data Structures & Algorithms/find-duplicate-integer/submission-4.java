class Solution {
    public int findDuplicate(int[] nums) {
        // 尋找快慢指針的相遇點
        int slow = nums[0];
        int fast = nums[0];
        
        do {
            slow = nums[slow];       // 走一步
            fast = nums[nums[fast]]; // 走兩步
        } while (slow != fast);

        // find the entrance （尋找環的入口）
        slow = nums[0];             // 慢指針回歸起點
        while (slow != fast) {
            slow = nums[slow];      // 走一步
            fast = nums[fast];      // 走一步
        }
        return slow; 
    }
}
