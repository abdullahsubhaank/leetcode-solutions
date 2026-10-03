class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else "#"
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    s = Solution()
    assert s.isValid("()[]{}") == True   # typical
    assert s.isValid("(]") == False      # edge: mismatched brackets
    print("All Valid Parentheses tests passed")