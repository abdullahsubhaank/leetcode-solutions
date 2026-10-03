from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]   # typical
    assert to_list(s.reverseList(build([7]))) == [7]                           # edge: single node
    print("All Reverse Linked List tests passed")