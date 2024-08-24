# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root, minnode, maxnode):
            if not root:
                return True
            elif minnode and root.val <= minnode.val:
                return False
            elif maxnode and root.val >= maxnode.val:
                return False
            
            # minnode and maxnode are universal values to compare to
            return rec(root.left, minnode, root) and rec(root.right, root, maxnode)
        return rec(root, None, None)
            