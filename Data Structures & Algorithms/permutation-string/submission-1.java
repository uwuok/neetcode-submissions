class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) { return false; }
        int[] s1_table = new int[26];
        for (int i = 0; i < s1.length(); ++i) {
            s1_table[s1.charAt(i) - 'a']++;
        }
        // window size 可以固定
        int[] s2_table = new int[26];
        int left = 0;
        for (int right = 0; right < s2.length(); ++right) {
            if (right >= s1.length()) {
                s2_table[s2.charAt(left) - 'a']--;
                ++left;
            }
            s2_table[s2.charAt(right) - 'a']++;
            if (check(s1_table, s2_table)) { return true; }
        }
        return false; 
    }

    private boolean check(int[] s1_table, int[] s2_table) {
        for (int i = 0; i < s1_table.length; ++i) {
            if (s1_table[i] != s2_table[i]) { return false;}
        }
        return true; 
    }
}
