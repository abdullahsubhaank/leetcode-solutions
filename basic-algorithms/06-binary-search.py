from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    assert s.search(nums, 9) == 4    # typical
    assert s.search(nums, 2) == -1   # edge: target not found
    print("All Binary Search tests passed")