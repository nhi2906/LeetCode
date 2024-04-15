class Solution(object):
    def maxProfit(self, prices):
        # buy low, sell high
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            right += 1
        return max_profit