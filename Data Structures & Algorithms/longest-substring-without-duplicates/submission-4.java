class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap(); // char, index
        int maxLength = 0; // 紀錄最長 substring 長度
        int left = 0;      // window left boundary 

        for (int right = 0; right < s.length(); ++right) {
            char currentChar = s.charAt(right);
            // 確認當前 char 是否在 map 中 以及 其是否不在當前的 window 中(不在當前 window 就可以視其沒有重複)
            if (map.containsKey(currentChar) && map.get(currentChar) >= left) {
                left = map.get(currentChar) + 1; 
            }
            map.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1); 
        }
        return maxLength; 
    }
}
