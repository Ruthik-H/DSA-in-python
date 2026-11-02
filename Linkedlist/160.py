
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create first linked list
head1 = ListNode(4)
head1.next = ListNode(1)
head1.next.next = ListNode(8)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

# Create second linked list
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(1)
head2.next.next.next = head1.next.next  # Shared node!

skip1 = 2
skip2 = 3

current1 = head1
current2 = head2

# Move to intersection starting positions
for i in range(skip1):
    current1 = current1.next

for j in range(skip2):
    current2 = current2.next

# Check intersection
if current1 is current2:
    print("Intersection found:", current1.val)
else:
    print("No intersection")
