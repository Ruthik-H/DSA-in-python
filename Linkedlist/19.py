# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length=0
        current=head
        while current is not None:
            length+=1
            current=current.next
        if n==length:
            return head.next

        slow=head
        steps=length-n-1
        for _ in range(steps):
            slow=slow.next
        slow.next=slow.next.next
        return head

        
        