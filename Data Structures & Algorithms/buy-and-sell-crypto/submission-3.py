class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        purchase = float('inf')
        gain = 0
        for day in range (0, len(prices)):
            currentPrice = prices[day]
            #NOTE: when a purchase is more convinient, the comparison window gets resetted. What is before this moment will be less convinient
            if currentPrice < purchase:
                purchase = currentPrice 
            else:
                gain = max(currentPrice - purchase, gain)

        return gain