# Problem: Two Sum (Easy)
**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

### Approach
A brute-force comparison of all pairs requires O(n^2) time. Instead, we use a one-pass hash map (`seen`) to store each number and its index as we traverse the array. For each element `num`, we check if its complement (`target - num`) already exists in the dictionary, allowing instantaneous O(1) lookups and finding the pair in a single pass.

### Complexity
- **Time:** O(n)
- **Space:** O(n)