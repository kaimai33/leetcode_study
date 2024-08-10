# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # return True if subtree has 1
        def rec(root):
            if not root:
                return None

            root.left = rec(root.left)
            root.right = rec(root.right)

            if root.left is None and root.right is None and root.val == 0:
                return None
            return root

        return rec(root)
            
            
