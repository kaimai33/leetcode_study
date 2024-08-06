# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # convert to an array
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        ans = 0
        for i in range(len(arr) // 2):
            ans = max(ans, arr[i] + arr[len(arr) - 1 - i])
        return ans