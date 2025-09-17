# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # APPROACH - 02
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)  # one node before head
        node = dummy

        while node.next:

            if node.next.val == val:
                # delete
                node.next = node.next.next
            else:
                # traverse node one ahead
                node = node.next
        
        return dummy.next  # returning head