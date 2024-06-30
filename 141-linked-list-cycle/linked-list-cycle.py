# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        tor = head
        rab = head
        # first phase cycle determination

        while rab and rab.next:
            tor = tor.next
            rab = rab.next.next
            
            if tor == rab:
                break
        else:
            return False
        
        # the second phase entrance finding
        tor = head

        while tor != rab :
            rab = rab.next
            tor = tor.next
        
        return tor
        