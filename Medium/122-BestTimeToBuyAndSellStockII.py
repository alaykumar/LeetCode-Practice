class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        # Loop through prices starting from day 1
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's
            if prices[i] > prices[i-1]:
                # Capture the profit by "buying" at i-1 and "selling" at i
                profit += prices[i] - prices[i-1]

        return profit
        


