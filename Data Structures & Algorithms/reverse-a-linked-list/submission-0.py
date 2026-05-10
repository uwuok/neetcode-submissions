# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        stk = []
        while cur:
            # prev = cur
            stk.append(cur.val)
            cur = cur.next
            # del prev
        print(stk)
        
        cur = head
        for i in range(len(stk) - 1, -1, -1):
            cur.val = stk[i]
            cur = cur.next
        
        return head