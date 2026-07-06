class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        purchaseDay = 0
        purchase = math.nan
        gain = 0
        for day in range (0, len(prices)):
            currentPrice = prices[day]
            if purchase is math.nan or currentPrice < purchase:
                purchase = currentPrice
                purchaseDay = day
            else:
                potentialGain = currentPrice - purchase
                gain = potentialGain if potentialGain > gain else gain

        return gain