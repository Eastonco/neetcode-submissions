class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minbuy = prices[0]
        for price in prices:
            maxP = max(maxP, price - minbuy)
            minbuy = min(minbuy, price)
        return maxP
        