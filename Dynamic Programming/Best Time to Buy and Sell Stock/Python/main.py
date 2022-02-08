class Solution:



    def maxProfit2(self, prices):
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]  # our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


if __name__ == "__main__":
    test_list = [2, 1, 3, 0, 5]
    print(f"The best margin is {Solution().maxProfit2(test_list)}")
