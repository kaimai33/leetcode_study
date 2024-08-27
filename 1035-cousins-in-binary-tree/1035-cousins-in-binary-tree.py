# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def findDepth(root, target, curr_lvl):
            if not root:
                return None
            if root.val == target:
                return curr_lvl
            if findDepth(root.left, target, curr_lvl + 1):
                return findDepth(root.left, target, curr_lvl + 1)
            if findDepth(root.right, target, curr_lvl + 1):
                return findDepth(root.right, target, curr_lvl + 1)
        def findParent(root, target, prev_parent):
            if not root:
                return None
            if root.val == target:
                return prev_parent
            if findParent(root.left, target, root.val):
                return findParent(root.left, target, root.val)
            if findParent(root.right, target, root.val):
                return findParent(root.right, target, root.val)
        x_depth = findDepth(root, x, 0)
        y_depth = findDepth(root, y, 0)
        if x_depth != y_depth:
            return False
        if findParent(root, x, None) == findParent(root, y, None):
            return False
        return True
        
