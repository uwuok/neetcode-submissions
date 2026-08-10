class Solution {
    public int characterReplacement(String s, int k) {
        // 紀錄每個字母的出現次數
        int[] count = new int[26]; // 記錄當前窗口內個字母出現的頻率
        int left = 0; // window left boundary 
        int maxCount = 0; // 歷史以來單一字母出現的最大頻率 (高水位線，只增加不減少)
        int maxLength = 0; // 最終要回傳的最長合法窗口長度
        for (int right = 0; right < s.length(); ++right) {
            // 1. 計算當前窗口的每個字母出現次數
            count[s.charAt(right) - 'A']++;
            // 比較 maxCount 與當前添加的 char 的出現次數，不需要重新 traversal 整個 count array
            maxCount = Math.max(maxCount, count[s.charAt(right) - 'A']);
            
            // 如果窗口的大小減去 maxCount 超過了 k
            // 表示窗口不合法
            while ((right - left + 1) - maxCount > k) {
                // 對窗口進行右移動
                count[s.charAt(left) - 'A']--;
                ++left;
            }
                     
            // 3. 當窗口合法時，更新 maxLength
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength; 
    }
}
