class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice=10000
        for price in prices:
            if price>minPrice:
                currentProfit=max(price-minPrice,0)
                maxProfit=max(currentProfit,maxProfit)
            else:
                minPrice=price
        return maxProfit

