# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode(0, head)
        right = head
        left = dummyNode
        while n > 0:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummyNode.next