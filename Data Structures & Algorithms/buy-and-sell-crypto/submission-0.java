class Solution {
    public int maxProfit(int[] prices) {
        
        int best = 0;
        for (int i = 0; i < prices.length; ++i) {
            for (int j = i + 1; j < prices.length; ++j) {
                int profit = prices[j] - prices[i];
                if (profit > best) { best = profit; }
            }
        }
        return best;
    }
}
