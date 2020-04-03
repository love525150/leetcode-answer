'''
买卖股票的最佳时机

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。
'''
class Solution:
    def maxProfit(self, prices:list) -> int:
        maxP = 0
        if len(prices) == 0:
            return maxP
        buyPrice = prices[0]
        sellPrice = -9999999
        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
                sellPrice = -9999999
            elif prices[i] > sellPrice and prices[i] > buyPrice:
                sellPrice = prices[i]
                maxP = max(maxP, sellPrice - buyPrice)
        
        return maxP

print(Solution().maxProfit([7,6,4,3,1]))