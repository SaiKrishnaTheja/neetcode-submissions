class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i=0
        j=1
        while i<len(prices)-1 and j<len(prices):
            if prices[i]<prices[j]:
                profit=prices[j]-prices[i]
                max_profit=max(max_profit,profit)
                j+=1
            else:
                i=j
                j+=1
        return max_profit

                
        