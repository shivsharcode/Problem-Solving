# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prev = ListNode(0, head)  # one node prev to head
        node = head

        while node is not None:
            
            # first node of linked list
            if node.val == val and node == head:
                head = node.next
                node = node.next
                continue
            

            # node of linked list
            if node.val == val:
                prev.next = node.next
                node = node.next
                continue

            prev = node
            node = node.next

        return head