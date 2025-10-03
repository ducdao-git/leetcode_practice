from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = p - min_price
                max_profit = profit if profit > max_profit else max_profit

        return max_profit
