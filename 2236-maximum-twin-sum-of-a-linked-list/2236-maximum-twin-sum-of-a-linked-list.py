# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # understand
        # return max twin sum
        # twin sum is the mirrored node in the list

        # match
        # linked list
        
        # plan
        # iterate over list to get len
        # if odd then set the last node as max_twin
        # 

        fast, slow = head, head
        list_len = 1
        max_twin = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            list_len += 2
        
        if not fast:
            list_len -= 1

        if list_len % 2 == 1:
            max_twin = slow.val
            slow = slow.next
        
        prev = None

        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        while prev:
            max_twin = max(max_twin, prev.val + head.val)
            head = head.next
            prev = prev.next
        
        return max_twin
        


        # reverse back





        


        
        