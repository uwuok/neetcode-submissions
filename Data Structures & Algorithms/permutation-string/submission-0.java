class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // 這題的 window size 可以固定
        // 所以只需要透過固定的 window size 去滑動配對 permutation 就好
        // if (s1.length() == 0 || s2.length() == 0) { return false; }
        if (s1.length() > s2.length()) { return false; }
        int s1_total = 0;
        for (int i = 0; i < s1.length(); ++i) {
            s1_total += s1.charAt(i);
        }
        int left = 0;
        int s2_total = 0; 
        for (int right = 0; right < s2.length(); ++right) {
            // System.out.println(s2.substring(left, right + 1));
            // ++left;
            // 
            if (right >= s1.length()) { 
                s2_total -= s2.charAt(left);
                ++left;
            }
            s2_total += s2.charAt(right);
            if (s1_total == s2_total) { return true; }

        }
        return false; 
    }
}
