class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the list of prices
        for i in range(len(prices)):
            # If the current price is lower than min_price, update min_price
            if prices[i] < min_price:
                min_price = prices[i]
            # Otherwise, check if selling at the current price gives a better profit
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price  # Update max profit
        
       
        return max_profit
