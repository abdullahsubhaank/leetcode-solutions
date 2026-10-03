from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]
    s.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]   # typical

    b = [0]
    s.moveZeroes(b)
    assert b == [0]                # edge: single zero
    print("All Move Zeroes tests passed")