class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        mid_idx=count//2
        for i in range(mid_idx):
            current=current.next
        return current
        