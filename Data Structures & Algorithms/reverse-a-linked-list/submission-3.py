# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            # 記錄 cur 的下一個位置
            temp = curr.next
            # 將 cur 的下一個位置改為 prev
            curr.next = prev
            # 將 prev 設為 cur (將 prev 往前移動)
            prev = curr
            # 將 cur 設為 temp (將 cur 往前移動)
            curr = temp
        return prev 