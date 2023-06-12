class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        lowest = prices[0]

        while r < len(prices):
            profit = prices[r] - prices [l]
            maxProfit = max(profit, maxProfit)
            if prices[r] < lowest:
                lowest = prices[r]
                l = r
                r +=1
            else:
                r += 1
        return maxProfit