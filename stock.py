class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        
        minprice=prices[0]
        maxprof=0
        for i in range(len(prices)):
            minprice=min(prices[i],minprice)
            maxprof=max(maxprof,prices[i]-minprice)
        return maxprof
