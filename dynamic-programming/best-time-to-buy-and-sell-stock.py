class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        curr_max = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                curr_max = max(curr_max, profit)
            else:
                left = right
            right += 1
        return curr_max