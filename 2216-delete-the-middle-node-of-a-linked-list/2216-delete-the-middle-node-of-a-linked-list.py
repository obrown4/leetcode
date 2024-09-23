# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # understand
        # delete the middle node of a linked list

        # match
        # temp head pattern

        # plan
        # create a curr ptr to head
        # iterate through the linked list keeping track of the size
        # then create new temp head and iterate till count = mid
        # stithc the nodes

        if not head.next:
            return None

        size = 0
        curr = head
        
        while curr:
            curr = curr.next
            size += 1

        mid = size // 2
        count = 0

        curr = head
        prev = None

        while count < mid:
            prev = curr
            curr = curr.next
            count += 1
        
        prev.next = curr.next
        return head