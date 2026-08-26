class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) { return false; }
        int[] count = new int[26];
        for (int i = 0; i < s1.length(); ++i) {
            count[s1.charAt(i) - 'a']++;
        }

        // sliding window
        for (int left = 0, right = 0; right < s2.length(); ++right) {
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
