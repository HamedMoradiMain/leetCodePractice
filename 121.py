class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if 0 in prices:prices.remove(0)
        if len(prices) > 2 and min(prices) == prices[-1]:
            prices.remove(prices[-1])
        if min(prices) != max(prices[prices.index(min(prices)):]):
            return  max(prices[prices.index(min(prices)):]) - min(prices)
        else:
            return 0
sol = Solution()
print(sol.maxProfit(prices = [3,2,6,5,0,3]))