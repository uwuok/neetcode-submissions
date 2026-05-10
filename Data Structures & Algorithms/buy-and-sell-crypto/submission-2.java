class Solution {
    public int maxProfit(int[] prices) {
        int buy = prices[0]; // 買點 (最好的買點就是最低的價格，因此我們要找到在 i 日前最低的價格)
        int best = 0; // 最好的價格
        // prices[i] 作為當前賣點
        for (int i = 0; i < prices.length; ++i) {
            // 如果出現更便宜的買點
            if (prices[i] < buy) { buy = prices[i]; }
            // 如果當前賣點可以獲取最大的利潤
            if (prices[i] - buy > best) { best = prices[i] - buy; }
        }
        return best;
    }
}
