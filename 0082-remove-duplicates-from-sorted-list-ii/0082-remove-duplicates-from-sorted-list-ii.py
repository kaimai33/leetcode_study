# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hmap = {}
        current = head

        while current:
            hmap[current.val] = hmap.get(current.val, 0) + 1
            current = current.next
        
        new_arr = []
        for key, val in hmap.items():
            if val == 1:
                new_arr.append(key)

        new_arr.sort()

        dummy = ListNode(0)
        ans = dummy

        for val in new_arr:
            ans.next = ListNode(val)
            ans = ans.next
        
        return dummy.next




