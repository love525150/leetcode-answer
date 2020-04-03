'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

思路：贪心算法，如果第二天比前一天小，马上在前一天卖出，第二天买入
证明： 
设有：a1 < a2, a2 > a3, a3 < a4，则：
(a2 - a1) + (a4 - a3) = (a4 - a1) + (a2 - a3) > a4 - a1
'''
class Solution:
    def maxProfit(self, prices: list) -> int:
        profit = 0
        if len(prices) == 0:
            return profit
        buyPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            else:
                buyPrice = prices[i]

        return profit

print(Solution().maxProfit([7,6,4,3,1]))