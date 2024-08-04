# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(rootp, rootq):
            if not rootp and not rootq:
                return True
            if not rootp or not rootq:
                return False
            if rootp.val != rootq.val:
                return False
            return rec(rootp.left, rootq.left) and rec(rootp.right, rootq.right)
        return rec(p, q)
