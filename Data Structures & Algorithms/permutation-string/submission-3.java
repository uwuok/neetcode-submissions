class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // window size 可以固定
        if (s1.length() > s2.length()) { return false; }
        // 透過 count 維護每個字母的數量
        // 如果是 s1 的字母則使用正數做統計
        // 反之為 s2 window 內的字母則使用負數做統計
        // 當 count 內的數值皆為 0 表示 s1 和 window 內字母對應的上
        int[] count = new int[26];
        for (int i = 0; i < s1.length(); ++i) {
            count[s1.charAt(i) - 'a']++;
        }

        // sliding window
        for (int left = 0, right = 0; right < s2.length(); ++right) {
            // window 移動，將原先已經計入的 window 字母移出 count 
            if (right - left + 1 > s1.length()) {
                count[s2.charAt(left) - 'a']++;
                ++left;
            }
            count[s2.charAt(right) - 'a']--;
            if (right - left + 1 == s1.length() && isZero(count)) {
                return true;
            }
        }
        return false; 
    }

    private boolean isZero(int[] count) {
        for (int n : count) {
            if (n != 0) { return false; }
        }
        return true; 
    }
}
