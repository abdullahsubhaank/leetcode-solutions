from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for col in range(len(strs[0])):
            char = strs[0][col]
            for row in range(1, len(strs)):
                if col == len(strs[row]) or strs[row][col] != char:
                    return strs[0][:col]
        return strs[0]
if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"   # typical
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""        # edge: no common prefix
    print("All Longest Common Prefix tests passed")