from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5   # typical
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0      # edge: prices only fall
    print("All Stock tests passed")