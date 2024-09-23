# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # understand
        # group linked list by odd and even indicies
        # return the head of the linked list
        # must use O(1) space and O(n) time
        # even nodes then odd nodes

        # match
        # traverse and stitch
        # temp head pattern

        # plan
        # odd = even = None
        # iterate through linked list
        # if index even then set even to node

        if not head:
            return None

        odd = ListNode()
        even = ListNode()

        odd_head = odd
        even_head = head

        index = 0
        while head:
            if index % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            
            head = head.next
            index += 1
        
        # stitch together
        odd.next = None
        even.next = odd_head.next

        return even_head

