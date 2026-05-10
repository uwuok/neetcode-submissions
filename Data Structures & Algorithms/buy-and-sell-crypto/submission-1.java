class Solution {
    public int maxProfit(int[] prices) {
        // 本質上找出最小和最大值即可
        // 但是因為時間的順序關係，因此
        int left = prices[0];
        int res = 0;
        for (int i = 0; i < prices.length; ++i) {
            if (prices[i] < left) { left = prices[i]; }
            if (prices[i] - left > res) { res = prices[i] - left; }
        }
        return res;
    }
}
