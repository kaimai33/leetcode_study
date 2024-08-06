# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        isConnected = False
        nums_set = set(nums)
        ans = 0
        while head:
            if head.val in nums_set:
                isConnected = True
            if head.val not in nums_set and isConnected:
                isConnected = False
                ans += 1
            head = head.next
        if isConnected:
            ans += 1
        return ans