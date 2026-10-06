# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = head
        while cur:
            new_node = cur.next
            cur.next = prev
            prev = cur
            cur = new_node
        return prev 
        