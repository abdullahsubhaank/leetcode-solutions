# Problem: Best Time to Buy and Sell Stock (Easy)
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Approach
One-pass tracking minimum price seen. We find the maximum profit from buying on one day and selling in the future by using a one-pass greedy approach that tracks the minimum price seen so far.
### Complexity
- **Time:** O(n)
- **Space:** O(1)