class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap(); // char, index
        int maxLength = 0; // 紀錄最長 substring 長度
        int left = 0;      // window left boundary 

        for (int right = 0; right < s.length(); ++right) {
            char currentChar = s.charAt(right);
            if (map.containsKey(currentChar) && map.get(currentChar) >= left) {
                left = map.get(currentChar) + 1; 
            }
            map.put(currentChar, right);
            maxLength = Math.max(maxLength, right - left + 1); 
        }
        return maxLength; 
    }
}
