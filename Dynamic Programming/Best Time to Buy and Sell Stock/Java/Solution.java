class Solution {
  public int maxProfit(int[] prices) {

    int localMinimum = 0;
    int localMaximum = 1;
    int maxMargin = 0;

    while (localMaximum < prices.length) {
      // If function decreasing
      if (prices[localMaximum] < prices[localMinimum]) {
        localMinimum = localMaximum;
      } else {
        // if function increasing
        maxMargin = Math.max((prices[localMaximum] - prices[localMinimum]), maxMargin);
      }
      localMaximum++;
    }
    return maxMargin;
  }
}